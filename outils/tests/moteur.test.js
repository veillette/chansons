/*
 * Tests du moteur : ordre des pages du livret, mélodies et partitions.
 *
 *     node --test outils/tests/
 *
 * Les scripts du site sont chargés tels quels dans un contexte où `window`
 * est l'objet global, comme dans le navigateur.
 */
"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const RACINE = path.resolve(__dirname, "..", "..");

function charger(...fichiers) {
  const contexte = {};
  contexte.window = contexte;
  vm.createContext(contexte);
  for (const f of fichiers) vm.runInContext(fs.readFileSync(path.join(RACINE, f), "utf8"), contexte, { filename: f });
  return contexte;
}

// Les tableaux créés dans le contexte vm ont un autre prototype Array :
// on les recopie avant de les comparer.
const hote = (valeur) => JSON.parse(JSON.stringify(valeur));

const { Imposition } = charger("js/imposition.js");
const { Melodie, Partition } = charger("js/melodie.js", "js/partition.js");

function chansons() {
  const liste = [];
  const dossier = path.join(RACINE, "chansons");
  for (const nom of fs.readdirSync(dossier).sort()) {
    const fichier = path.join(dossier, nom, "chanson.js");
    if (!fs.existsSync(fichier)) continue;
    vm.runInNewContext(fs.readFileSync(fichier, "utf8"), { Chansonnier: { ajouter: (c) => liste.push(c) } });
  }
  return liste;
}

const pages = (n, dernier = "quatrieme") =>
  Array.from({ length: n }, (_, i) => ({ type: i === 0 ? "couverture" : i === n - 1 ? dernier : undefined }));

/* ---------- Imposition ---------- */

test("livret de 8 pages : l'exemple de js/imposition.js", () => {
  const feuilles = Imposition.livret(pages(8));
  assert.deepEqual(
    hote(feuilles.map((f) => [f.recto, f.verso])),
    [
      [[7, 0], [1, 6]],
      [[5, 2], [3, 4]],
    ]
  );
});

test("les pages blanches vont avant la quatrième de couverture", () => {
  assert.deepEqual(hote(Imposition.completer(pages(6))), [0, 1, 2, 3, 4, null, null, 5]);
  assert.deepEqual(hote(Imposition.completer(pages(6, "texte"))), [0, 1, 2, 3, 4, 5, null, null]);
  assert.deepEqual(hote(Imposition.completer(pages(4))), [0, 1, 2, 3]);
});

test("pour toute longueur, chaque page est imprimée une fois et le pli tombe juste", () => {
  for (let n = 1; n <= 60; n++) {
    const feuilles = Imposition.livret(pages(n));
    const faces = feuilles.flatMap((f) => [...f.recto, ...f.verso]);
    assert.equal(faces.length % 4, 0, `${n} pages`);
    assert.deepEqual(
      hote(faces.filter((p) => p != null).sort((a, b) => a - b)),
      Array.from({ length: n }, (_, i) => i),
      `${n} pages`
    );
    // Livret plié : la couverture est la première page et la quatrième la dernière.
    const ordre = Imposition.completer(pages(n));
    assert.equal(feuilles[0].recto[1], 0);
    assert.equal(feuilles[0].recto[0], ordre[ordre.length - 1]);
    // Sur chaque face, les deux pages sont symétriques autour du pli.
    const m = ordre.length;
    feuilles.forEach((f, k) => {
      assert.deepEqual(hote(f.recto), [ordre[m - 1 - 2 * k], ordre[2 * k]]);
      assert.deepEqual(hote(f.verso), [ordre[2 * k + 1], ordre[m - 2 - 2 * k]]);
    });
  }
});

/* ---------- Mélodie ---------- */

test("analyser : hauteurs, altérations, durées et silences", () => {
  const [la, re, fa, sil, si] = Melodie.analyser("la4 ré4:0.5 | fa#5:2 -:1.5 sib3");
  assert.equal(la.frequence, 440);
  assert.equal(re.nom, "re");
  assert.equal(re.duree, 0.5);
  assert.equal(fa.alteration, 1);
  assert.equal(fa.octave, 5);
  assert.equal(sil.frequence, null);
  assert.equal(sil.duree, 1.5);
  assert.equal(si.alteration, -1);
  assert.ok(Math.abs(si.frequence - 233.08) < 0.01);
  assert.throws(() => Melodie.analyser("do4 ut4"), /ut4/);
});

/* ---------- Partition ---------- */

test("une note qui dépasse la barre est coupée en deux notes liées", () => {
  const abc = Partition.versAbc({ mesure: "4/4", notes: "do4 ré4 mi4 fa#4 | fa4:3 sol4:2 | sol4:4" });
  assert.match(abc, /C2 D2 E2 \^F2 \|/);
  // Nouvelle mesure : le fa redevient naturel sans bécarre ; le sol est lié par-dessus la barre.
  assert.match(abc, /F6 G2- \| G2/);
  assert.match(abc, /\|\]$/);
});

test("bécarre quand la même note revient sans altération dans la mesure", () => {
  assert.match(Partition.versAbc({ notes: "fa#4 fa4 sol4 sol4" }), /\^F2 =F2 G2 G2/);
});

test("anacrouse : première et dernière mesures raccourcies", () => {
  const mesures = Partition.mesures({ mesure: "2/4", anacrouse: 0.5, notes: "do4:0.5 ré4:2 mi4:1.5" });
  assert.deepEqual(
    hote(mesures.map((m) => m.reduce((t, e) => t + e.longueur, 0))),
    [1, 4, 3]
  );
});

test("6/8 : croches groupées par trois et durées ternaires", () => {
  const abc = Partition.versAbc({ mesure: "6/8", notes: "do4:0.5 ré4:0.5 mi4:0.5 fa4:1.5 | sol4:2.5 la4:0.5" });
  assert.match(abc, /M:6\/8/);
  assert.match(abc, /CDE F3 \| G3- G2A \|\]/);
});

test("syllabes : tirets, prolongations, ponctuation et guillemets", () => {
  const unites = Partition.syllabes("Ah ! vi-te~al-lons _ * « oui");
  assert.deepEqual(
    hote(unites.map((u) => u.texte + u.suite)),
    ["Ah~! ", "vi-", "te~al-", "lons ", "_ ", "* ", "«~oui "]
  );
});

test("chaque chanson donne une partition dont les paroles tombent juste", () => {
  for (const chanson of chansons()) {
    const melodie = chanson.melodie;
    if (!melodie) continue;
    const nom = chanson.id;
    const abc = Partition.versAbc(melodie);
    assert.match(abc, /\|\]$/m, nom);

    // Toutes les mesures pleines, sauf l'anacrouse et la dernière qui la complète.
    const [n, d] = (melodie.mesure || "4/4").split("/").map(Number);
    const barre = (n * 8) / d; // en croches
    const longueurs = Partition.mesures(melodie).map((m) => m.reduce((t, e) => t + e.longueur, 0));
    const anacrouse = (melodie.anacrouse || 0) * 2;
    longueurs.forEach((l, i) => {
      let attendu = barre;
      if (anacrouse && i === 0) attendu = anacrouse;
      else if (anacrouse && i === longueurs.length - 1) attendu = barre - anacrouse;
      assert.ok(Math.abs(l - attendu) < 1e-9, `${nom} : mesure ${i + 1} de ${l} croches au lieu de ${attendu}`);
    });

    // Le premier couplet a une syllabe par note.
    const couplets = Partition.couplets(melodie);
    if (couplets.length) {
      assert.equal(Partition.syllabes(couplets[0]).length, Partition.nombreDeNotes(melodie), nom);
    }

    // Le découpage en pages (js/chansons.js) couvre toutes les portées.
    assert.ok(Partition.lignes(melodie) >= 1, nom);
  }
});
