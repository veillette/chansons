/*
 * Mélodie : joue l'air d'une chanson avec le synthétiseur du navigateur
 * (Web Audio), avec un timbre doux de piano feutré.
 *
 * Notation (champ `melodie` d'une chanson) :
 *   { tempo: 100, notes: "do4 do4 do4 ré4 | mi4:2 ré4:2 | do4 mi4 ré4 ré4 | do4:4" }
 *   - une note : do ré mi fa sol la si, puis # (dièse) ou b (bémol) facultatif,
 *     puis l'octave (4 = octave du do central ; par défaut 4) ;
 *   - « :durée » en temps (défaut 1 ; 0.5 = croche, 2 = blanche, 1.5 = noire pointée) ;
 *   - « - » est un silence (« -:2 » = deux temps) ;
 *   - « | » (barre de mesure) sert seulement à la lecture et est ignorée.
 *   `tempo` : nombre de temps par minute (défaut 100).
 */
(function () {
  "use strict";

  const DEMI_TONS = { do: 0, re: 2, mi: 4, fa: 5, sol: 7, la: 9, si: 11 };
  const NOTE = /^(do|r[eé]|mi|fa|sol|la|si)(#|b)?(\d)?(?::(\d+(?:\.\d+)?))?$/;
  const SILENCE = /^-(?::(\d+(?:\.\d+)?))?$/;

  /* Transforme le texte en une liste de { frequence (null = silence), duree en temps }.
     Chaque note garde aussi son nom (do…si), son altération (-1, 0, 1) et son
     octave, pour la partition (js/partition.js). */
  function analyser(texte) {
    const notes = [];
    String(texte || "")
      .split(/\s+/)
      .filter((t) => t && t !== "|")
      .forEach((jeton) => {
        let m = jeton.match(SILENCE);
        if (m) {
          notes.push({ frequence: null, duree: Number(m[1] || 1) });
          return;
        }
        m = jeton.match(NOTE);
        if (!m) throw new Error(`Note inconnue dans la mélodie : « ${jeton} »`);
        const nom = m[1].replace("é", "e");
        const alteration = m[2] === "#" ? 1 : m[2] === "b" ? -1 : 0;
        const octave = m[3] ? Number(m[3]) : 4;
        // la4 = 440 Hz, soit 9 demi-tons au-dessus de do4.
        const midi = 12 * (octave + 1) + DEMI_TONS[nom] + alteration;
        notes.push({ frequence: 440 * Math.pow(2, (midi - 69) / 12), duree: Number(m[4] || 1), nom, alteration, octave });
      });
    return notes;
  }

  const DUREE_ECHANTILLON = 4;
  const echantillons = new Map();
  let contexte = null;
  let enCours = null; // { sortie, sources, minuterie, fin }

  /* Un échantillon par hauteur, réutilisé pour chaque occurrence de la note.
     Les harmoniques aiguës s'éteignent plus vite, comme sur un instrument frappé. */
  function echantillon(frequence) {
    if (echantillons.has(frequence)) return echantillons.get(frequence);
    const taux = Math.min(contexte.sampleRate, 24000);
    const taille = Math.ceil(DUREE_ECHANTILLON * taux);
    const tampon = contexte.createBuffer(1, taille, taux);
    const donnees = tampon.getChannelData(0);
    const harmoniques = [
      [1, 1, 2.1],
      [1.997, 0.22, 1.7],
      [2.003, 0.24, 1.15],
      [3.006, 0.09, 0.62],
      [4.018, 0.035, 0.36],
    ].filter(([multiple]) => frequence * multiple < taux * 0.45);
    let graine = 12345;
    for (let i = 0; i < taille; i++) {
      const t = i / taux;
      let valeur = 0;
      for (const [multiple, amplitude, decroissance] of harmoniques) {
        valeur += amplitude * Math.exp(-t / decroissance) * Math.sin(2 * Math.PI * frequence * multiple * t);
      }
      // Le léger bruit initial évoque le contact du marteau avec la corde.
      graine = (Math.imul(graine, 1664525) + 1013904223) >>> 0;
      valeur += ((graine / 4294967296) * 2 - 1) * 0.045 * Math.exp(-t / 0.012);
      const attaque = Math.min(1, t / 0.004);
      const fin = Math.min(1, (DUREE_ECHANTILLON - t) / 0.18);
      donnees[i] = valeur * attaque * fin * 0.58;
    }
    echantillons.set(frequence, tampon);
    return tampon;
  }

  /* Petite réverbération stéréo calculée une seule fois, sans fichier ni réseau. */
  let impulsion = null;
  function reverberation() {
    if (impulsion) return impulsion;
    const taux = contexte.sampleRate;
    const taille = Math.ceil(0.9 * taux);
    impulsion = contexte.createBuffer(2, taille, taux);
    for (let canal = 0; canal < 2; canal++) {
      const donnees = impulsion.getChannelData(canal);
      let graine = 731 + canal * 97;
      for (let i = 0; i < taille; i++) {
        const t = i / taux;
        graine = (Math.imul(graine, 1664525) + 1013904223) >>> 0;
        // Une courte prédélai laisse chaque attaque bien distincte.
        donnees[i] = t < 0.022 ? 0 : ((graine / 4294967296) * 2 - 1) * Math.exp(-t * 7) * 0.12;
      }
    }
    return impulsion;
  }

  function disponible() {
    return Boolean(window.AudioContext || window.webkitAudioContext);
  }

  function arreter() {
    if (!enCours) return;
    const { sortie, sources, minuterie, fin } = enCours;
    enCours = null;
    clearTimeout(minuterie);
    const t = contexte.currentTime;
    sortie.gain.cancelScheduledValues(t);
    sortie.gain.setValueAtTime(sortie.gain.value, t);
    sortie.gain.linearRampToValueAtTime(0, t + 0.05);
    for (const source of sources) {
      try { source.stop(t + 0.06); } catch { /* déjà terminée */ }
    }
    setTimeout(() => sortie.disconnect(), 100);
    fin();
  }

  /* Joue la mélodie ; la promesse est résolue à la fin ou à l'arrêt. */
  function jouer(melodie) {
    arreter();
    if (!melodie || !disponible()) return Promise.resolve();
    let notes;
    try {
      notes = analyser(melodie.notes);
    } catch (err) {
      // Une mélodie mal écrite ne doit pas bloquer les boutons (outils/verifier.py la signale).
      console.error(err);
      return Promise.resolve();
    }
    const temps = 60 / (melodie.tempo || 100);

    contexte = contexte || new (window.AudioContext || window.webkitAudioContext)();
    if (contexte.state === "suspended") contexte.resume();

    const sortie = contexte.createGain();
    sortie.gain.value = 0.32;
    const sec = contexte.createGain();
    sec.gain.value = 0.9;
    sec.connect(sortie);
    const effet = contexte.createConvolver();
    effet.buffer = reverberation();
    const filtre = contexte.createBiquadFilter();
    filtre.type = "lowpass";
    filtre.frequency.value = 3200;
    const humide = contexte.createGain();
    humide.gain.value = 0.12;
    effet.connect(filtre).connect(humide).connect(sortie);
    sortie.connect(contexte.destination);

    // Préparer les hauteurs avant de fixer l'heure de départ : sur un appareil
    // lent, leur calcul ne doit pas comprimer les premières notes.
    for (const note of notes) if (note.frequence) echantillon(note.frequence);
    let t = contexte.currentTime + 0.08;
    let finSon = t;
    const sources = [];
    // La dernière note résonne au moins un temps, même raccourcie par l'anacrouse.
    const derniere = notes.map((n) => n.frequence != null).lastIndexOf(true);
    notes.forEach((note, i) => {
      const duree = note.duree * temps;
      if (note.frequence) {
        const sonne = i === derniere ? Math.max(duree, temps) : duree;
        const source = contexte.createBufferSource();
        const env = contexte.createGain();
        source.buffer = echantillon(note.frequence);
        const fin = t + Math.min(sonne, DUREE_ECHANTILLON - 0.02);
        const relachement = Math.min(0.12, sonne * 0.25);
        env.gain.setValueAtTime(0, t);
        env.gain.linearRampToValueAtTime(1, t + 0.006);
        env.gain.setValueAtTime(1, Math.max(t + 0.006, fin - relachement));
        env.gain.linearRampToValueAtTime(0, fin);
        source.connect(env);
        env.connect(sec);
        env.connect(effet);
        source.start(t);
        source.stop(fin);
        sources.push(source);
        finSon = Math.max(finSon, fin);
      }
      t += duree;
    });

    return new Promise((resolve) => {
      const total = (Math.max(t, finSon) - contexte.currentTime + 0.9) * 1000;
      enCours = { sortie, sources, fin: resolve, minuterie: setTimeout(() => {
        enCours = null;
        sortie.disconnect();
        resolve();
      }, total) };
    });
  }

  window.Melodie = { analyser, jouer, arreter, disponible, joue: () => enCours != null };
})();
