/*
 * Mélodie : joue l'air d'une chanson avec le synthétiseur du navigateur
 * (Web Audio), avec un son doux de boîte à musique.
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

  let contexte = null;
  let enCours = null; // { sortie, minuterie, fin }

  function disponible() {
    return Boolean(window.AudioContext || window.webkitAudioContext);
  }

  function arreter() {
    if (!enCours) return;
    const { sortie, minuterie, fin } = enCours;
    enCours = null;
    clearTimeout(minuterie);
    const t = contexte.currentTime;
    sortie.gain.cancelScheduledValues(t);
    sortie.gain.setValueAtTime(sortie.gain.value, t);
    sortie.gain.linearRampToValueAtTime(0, t + 0.05);
    setTimeout(() => sortie.disconnect(), 100);
    fin();
  }

  /* Joue la mélodie ; la promesse est résolue à la fin ou à l'arrêt. */
  function jouer(melodie) {
    arreter();
    if (!melodie || !disponible()) return Promise.resolve();
    const notes = analyser(melodie.notes);
    const temps = 60 / (melodie.tempo || 100);

    contexte = contexte || new (window.AudioContext || window.webkitAudioContext)();
    if (contexte.state === "suspended") contexte.resume();

    const sortie = contexte.createGain();
    sortie.gain.value = 0.25;
    sortie.connect(contexte.destination);

    let t = contexte.currentTime + 0.08;
    for (const note of notes) {
      const duree = note.duree * temps;
      if (note.frequence) {
        // Fondamentale (triangle) + une octave au-dessus très discrète (sinus).
        [
          ["triangle", 1, 0.9],
          ["sine", 2, 0.18],
        ].forEach(([forme, multiple, volume]) => {
          const osc = contexte.createOscillator();
          const env = contexte.createGain();
          osc.type = forme;
          osc.frequency.value = note.frequence * multiple;
          env.gain.setValueAtTime(0.0001, t);
          env.gain.exponentialRampToValueAtTime(volume, t + 0.015);
          env.gain.exponentialRampToValueAtTime(volume * 0.35, t + Math.min(0.25, duree * 0.6));
          env.gain.exponentialRampToValueAtTime(0.0001, t + duree * 0.97);
          osc.connect(env).connect(sortie);
          osc.start(t);
          osc.stop(t + duree);
        });
      }
      t += duree;
    }

    return new Promise((resolve) => {
      const total = (t - contexte.currentTime) * 1000;
      enCours = { sortie, fin: resolve, minuterie: setTimeout(() => {
        enCours = null;
        sortie.disconnect();
        resolve();
      }, total + 100) };
    });
  }

  window.Melodie = { analyser, jouer, arreter, disponible, joue: () => enCours != null };
})();
