/*
 * Partition : dessine la mélodie d'une chanson sur une portée, avec les paroles
 * sous les notes, grâce à la bibliothèque abcjs (lib/abcjs/, licence MIT).
 *
 * La mélodie est écrite dans la notation de js/melodie.js ; on la convertit en
 * notation ABC. Champs de `melodie` utilisés en plus de `notes` :
 *   - mesure : "4/4", "3/4", "2/4", "6/8"… (4/4 par défaut) ;
 *   - anacrouse : nombre de temps avant la première barre de mesure (0 par défaut) ;
 *   - syllabes : un couplet par chaîne, une syllabe par note (les silences n'en
 *     prennent pas). Les mots sont séparés par des espaces et les syllabes d'un
 *     mot par « - » ; « _ » prolonge la syllabe précédente sur une note de plus,
 *     « * » laisse une note sans paroles, « ~ » réunit deux mots sous une note ;
 *   - mesuresParLigne : nombre de mesures par portée (par défaut, selon le
 *     nombre de notes : de 2 à 4).
 * Les barres de mesure sont calculées ; les « | » de `notes` ne servent qu'à relire.
 * Une note qui dépasse la barre est coupée en deux notes liées.
 */
(function () {
  "use strict";

  const LETTRES = { do: "C", re: "D", mi: "E", fa: "F", sol: "G", la: "A", si: "B" };
  // Durées écrivables en ABC, en croches (L:1/8), de la plus longue à la plus courte.
  // En 6/8 (temps de 3 croches), pas de blanche : 5 croches = noire pointée + noire.
  const LONGUEURS = [8, 6, 4, 3, 2, 1.5, 1, 0.5];
  const LONGUEURS_TERNAIRES = [6, 3, 2, 1.5, 1, 0.5];
  // Mise en page (unités d'abcjs) : largeur des portées, place laissée aux
  // notes après la clé, et largeur moyenne d'une lettre des paroles.
  const LARGEUR_PORTEE = 600;
  const LARGEUR_UTILE = 560;
  const TAILLE_PAROLES = 14; // points ; 1 pt = 4/3 unités
  const CHASSE = ((TAILLE_PAROLES * 4) / 3) * 0.45; // largeur moyenne d'une lettre d'Andika
  const TETE = 20; // place minimale d'une note

  function lireMesure(melodie) {
    const m = String(melodie.mesure || "4/4").match(/^(\d+)\/(\d+)$/);
    const [n, d] = m ? [Number(m[1]), Number(m[2])] : [4, 4];
    return {
      texte: `${n}/${d}`,
      barre: (n * 8) / d, // longueur d'une mesure, en croches
      // Les croches sont groupées par temps : 3 croches en 6/8, 9/8, 12/8.
      groupe: d === 8 && n % 3 === 0 ? 3 : 8 / d,
    };
  }

  function decomposer(longueur, ternaire) {
    const morceaux = [];
    let reste = longueur;
    while (reste > 1e-9) {
      const l = (ternaire ? LONGUEURS_TERNAIRES : LONGUEURS).find((x) => x <= reste + 1e-9);
      if (!l) break;
      morceaux.push(l);
      reste -= l;
    }
    return morceaux;
  }

  function hauteur(note) {
    let lettre = LETTRES[note.nom];
    if (note.octave >= 5) lettre = lettre.toLowerCase() + "'".repeat(note.octave - 5);
    else lettre += ",".repeat(4 - note.octave);
    return lettre;
  }

  function texteLongueur(l) {
    return l === 1 ? "" : l === 0.5 ? "/2" : l === 1.5 ? "3/2" : String(l);
  }

  /* Découpe la mélodie en mesures. Chaque évènement : { note (null = silence),
     longueur en croches, debut dans la mesure, lie (liée à la suivante),
     syllabe (première partie d'une note : reçoit une syllabe) }. */
  function mesures(melodie) {
    const { barre, groupe } = lireMesure(melodie);
    const resultat = [[]];
    let capacite = melodie.anacrouse ? melodie.anacrouse * 2 : barre;
    let pos = 0;
    window.Melodie.analyser(melodie.notes).forEach((note) => {
      const silence = note.frequence == null;
      let reste = note.duree * 2;
      let premiere = true;
      while (reste > 1e-9) {
        const morceau = Math.min(reste, capacite - pos);
        reste -= morceau;
        const parts = decomposer(morceau, groupe === 3);
        parts.forEach((l, i) => {
          resultat[resultat.length - 1].push({
            note: silence ? null : note,
            longueur: l,
            debut: pos,
            lie: !silence && (reste > 1e-9 || i < parts.length - 1),
            syllabe: !silence && premiere,
          });
          premiere = false;
          pos += l;
        });
        if (pos >= capacite - 1e-9) {
          resultat.push([]);
          pos = 0;
          capacite = barre;
        }
      }
    });
    if (!resultat[resultat.length - 1].length) resultat.pop();
    return resultat;
  }

  /* Les syllabes d'un couplet : [{ texte, suite: "-" (le mot continue) ou " " }].
     Même découpage que outils/verifier.py (syllabes). */
  function syllabes(couplet) {
    const unites = [];
    let prefixe = "";
    String(couplet || "")
      .trim()
      .split(/\s+/)
      .filter(Boolean)
      .forEach((mot) => {
        // Ponctuation isolée (« Ah ! ») : collée à la syllabe voisine par une espace insécable.
        if (/^[!?;:,.»…]+$/.test(mot) && unites.length) {
          unites[unites.length - 1].texte += `~${mot}`;
          return;
        }
        if (mot === "«") {
          prefixe = "«~";
          return;
        }
        if (mot === "_" || mot === "*") {
          unites.push({ texte: mot, suite: " " });
          return;
        }
        const parts = mot.split("-").filter(Boolean);
        parts.forEach((p, i) => {
          unites.push({ texte: (i === 0 ? prefixe : "") + p, suite: i < parts.length - 1 ? "-" : " " });
          if (i === 0) prefixe = "";
        });
      });
    return unites;
  }

  /* Nombre de notes qui reçoivent une syllabe (les silences et les notes liées n'en reçoivent pas). */
  function nombreDeNotes(melodie) {
    return window.Melodie.analyser(melodie.notes).filter((n) => n.frequence != null).length;
  }

  function couplets(melodie) {
    const s = melodie.syllabes;
    return Array.isArray(s) ? s : s ? [s] : [];
  }

  /* Les portées : [{ abc (musique), notes (nombre de syllabes à placer) }]. */
  function portees(melodie) {
    const { groupe } = lireMesure(melodie);
    const liste = mesures(melodie);
    const lignes = [];
    // L'anacrouse reste sur la première portée, en plus de ses mesures pleines.
    const anacrouse = melodie.anacrouse ? 1 : 0;
    if (melodie.mesuresParLigne) {
      for (let i = 0; i < liste.length; ) {
        const n = melodie.mesuresParLigne + (i === 0 ? anacrouse : 0);
        lignes.push(liste.slice(i, i + n));
        i += n;
      }
    } else {
      // Au plus 4 mesures par portée, et pas plus que la largeur de la portée.
      // abcjs avance de k × √durée après chaque note (layout/voice-elements.js)
      // et des syllabes trop serrées se chevauchent : k doit laisser à chaque
      // note la place de sa plus longue syllabe. Puis les mesures sont réparties à
      // peu près également, pour que la dernière portée ne reste pas presque vide.
      const vers = couplets(melodie).map(syllabes);
      let rang = 0;
      const notes = liste.map((mesure) =>
        mesure.map((ev) => {
          let texte = 0;
          if (ev.note && ev.syllabe) {
            texte = Math.max(0, ...vers.map((v) => (v[rang] ? v[rang].texte.length : 0))) * CHASSE + 7;
            rang++;
          }
          return { duree: ev.longueur, texte };
        })
      );
      const largeurLigne = (debut, fin) => {
        const ligne = notes.slice(debut, fin).flat();
        const k = Math.max(TETE, ...ligne.map((n) => n.texte / Math.sqrt(n.duree)));
        return ligne.reduce((t, n) => t + Math.max(TETE, k * Math.sqrt(n.duree)), 0) + 12 * (fin - debut);
      };
      const couper = (limite) => {
        const resultat = [];
        let debut = 0;
        for (let i = 1; i < liste.length; i++) {
          const pleines = i - debut - (resultat.length === 0 ? anacrouse : 0);
          if (pleines >= 4 || (pleines >= 1 && largeurLigne(debut, i + 1) > limite)) {
            resultat.push([debut, i]);
            debut = i;
          }
        }
        resultat.push([debut, liste.length]);
        return resultat;
      };
      let decoupe = couper(LARGEUR_UTILE);
      const nb = decoupe.length;
      const somme = decoupe.reduce((t, [debut, fin]) => t + largeurLigne(debut, fin), 0);
      for (let limite = Math.ceil(somme / nb); limite < LARGEUR_UTILE; limite += 10) {
        const essai = couper(limite);
        if (essai.length === nb) {
          decoupe = essai;
          break;
        }
      }
      decoupe.forEach(([debut, fin]) => lignes.push(liste.slice(debut, fin)));
    }
    return lignes.map((groupeMesures, numero) => {
      let nbNotes = 0;
      const texte = groupeMesures
        .map((evenements, m) => {
          const alterees = {};
          const musique = evenements
            .map((ev, i) => {
              // Une espace avant chaque temps : les croches d'un même temps sont ligaturées.
              const espace = i > 0 && Math.abs(ev.debut % groupe) < 1e-9 ? " " : "";
              if (!ev.note) return `${espace}z${texteLongueur(ev.longueur)}`;
              if (ev.syllabe) nbNotes++;
              const h = hauteur(ev.note);
              let signe = "";
              if (ev.note.alteration) signe = ev.note.alteration > 0 ? "^" : "_";
              else if (alterees[h]) signe = "=";
              alterees[h] = ev.note.alteration !== 0;
              return `${espace}${signe}${h}${texteLongueur(ev.longueur)}${ev.lie ? "-" : ""}`;
            })
            .join("");
          const derniere = numero === lignes.length - 1 && m === groupeMesures.length - 1;
          return `${musique} ${derniere ? "|]" : "|"}`;
        })
        .join(" ");
      return { abc: texte, notes: nbNotes };
    });
  }

  function ligneParoles(unites) {
    return unites
      .map((u) => u.texte.replace(/[|%\\]/g, "") + u.suite)
      .join("")
      .trim();
  }

  /* Le texte ABC des portées [debut, fin[ (toutes par défaut). */
  function versAbc(melodie, { debut = 0, fin = Infinity } = {}) {
    const lignes = portees(melodie);
    const vers = couplets(melodie).map(syllabes);
    const curseurs = vers.map(() => 0);
    const corps = [];
    lignes.forEach((ligne, i) => {
      const morceaux = vers.map((unites, c) => {
        const tranche = unites.slice(curseurs[c], curseurs[c] + ligne.notes);
        curseurs[c] += ligne.notes;
        return tranche;
      });
      if (i < debut || i >= fin) return;
      corps.push(ligne.abc);
      morceaux.forEach((tranche) => {
        if (tranche.length) corps.push(`w: ${ligneParoles(tranche)}`);
      });
    });
    return ["X:1", `M:${lireMesure(melodie).texte}`, "L:1/8", "K:C", ...corps].join("\n");
  }

  function lignes(melodie) {
    return portees(melodie).length;
  }

  /* Dessine les portées [debut, fin[ de la mélodie dans le conteneur. */
  function dessiner(conteneur, melodie, options = {}, policeAttendue = false) {
    if (!window.ABCJS) {
      conteneur.textContent = "La partition n'a pas pu être chargée.";
      return;
    }
    // abcjs mesure les textes : la page doit être dans le document et la police
    // des paroles chargée. Sinon, on dessine dans un coin caché, puis on redessine
    // quand la police est arrivée.
    const police = `${TAILLE_PAROLES}px Andika`;
    const detache = !conteneur.isConnected;
    let parent, suivant;
    if (detache) {
      ({ parentNode: parent, nextSibling: suivant } = conteneur);
      reserve().appendChild(conteneur);
    }
    rendre(conteneur, melodie, options);
    if (detache) {
      if (parent) parent.insertBefore(conteneur, suivant);
      else conteneur.remove();
    }
    if (!policeAttendue && document.fonts && !document.fonts.check(police)) {
      document.fonts.load(police).then(() => dessiner(conteneur, melodie, options, true));
    }
  }

  let coin = null;
  function reserve() {
    if (!coin || !coin.isConnected) {
      coin = document.createElement("div");
      coin.setAttribute("aria-hidden", "true");
      coin.style.cssText = "position:absolute;left:-10000px;top:0;width:800px;visibility:hidden";
      document.body.appendChild(coin);
    }
    return coin;
  }

  /* Dessin à taille fixe, puis viewBox : la feuille de style met la partition
     à la largeur de la page et la réduit si elle est trop haute. */
  function rendre(conteneur, melodie, options) {
    window.ABCJS.renderAbc(conteneur, versAbc(melodie, options), {
      staffwidth: LARGEUR_PORTEE,
      paddingtop: 4,
      paddingbottom: 4,
      paddingleft: 4,
      paddingright: 4,
      add_classes: true,
      format: {
        vocalfont: `Andika ${TAILLE_PAROLES}`,
        annotationfont: "Andika 12",
        vocalspace: 4,
        stretchlast: true, // la dernière portée aussi : sinon ses syllabes se serrent
      },
    });
    conteneur.removeAttribute("style");
    const svg = conteneur.querySelector("svg");
    if (!svg) return;
    const largeur = parseFloat(svg.getAttribute("width"));
    const hauteur = parseFloat(svg.getAttribute("height"));
    if (!svg.getAttribute("viewBox") && largeur && hauteur) svg.setAttribute("viewBox", `0 0 ${largeur} ${hauteur}`);
    svg.removeAttribute("width");
    svg.removeAttribute("height");
    svg.removeAttribute("style");
  }

  window.Partition = { versAbc, dessiner, lignes, syllabes, nombreDeNotes, couplets, mesures };
})();
