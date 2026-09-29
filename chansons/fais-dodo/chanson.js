Chansonnier.ajouter({
  id: "fais-dodo",
  titre: "Fais dodo",
  sousTitre: "Colas, mon p'tit frère",
  auteur: "Berceuse traditionnelle",
  age: "0 à 4 ans",
  genre: "Berceuse",
  couleur: "#1971c2",
  vignette: "images/vignette.svg",
  resume:
    "Pendant que Maman fait du gâteau et que Papa fait du chocolat, la grande sœur berce " +
    "le petit Colas. Une berceuse très douce, à chanter tout bas au moment du coucher.",
  melodie: {
    tempo: 72,
    mesure: "2/4",
    notes:
      "mi4:0.5 do4:0.5 mi4 | do4:0.5 mi4:0.5 fa4:0.5 sol4:0.5 | fa4 mi4 | " +
      "ré4:0.5 si3:0.5 ré4 | si3:0.5 ré4:0.5 mi4:0.5 fa4:0.5 | ré4:2 | " +
      "mi4:0.5 mi4:0.5 mi4:0.5 fa4:0.5 | sol4:2 | mi4:0.5 mi4:0.5 mi4:0.5 fa4:0.5 | sol4:2 | " +
      "ré4:0.5 ré4:0.5 ré4:0.5 mi4:0.5 | fa4:2 | ré4:0.5 ré4:0.5 ré4:0.5 mi4:0.5 | fa4 mi4 | " +
      "mi4:0.5 do4:0.5 mi4 | do4:0.5 mi4:0.5 fa4:0.5 sol4:0.5 | fa4 mi4 | " +
      "ré4:0.5 si3:0.5 ré4 | si3:0.5 ré4:0.5 mi4:0.5 ré4:0.5 | do4:2",
    syllabes: [
      "Fais do-do, Co-las mon p'tit frè-re, Fais do-do, t'au-ras du lo-lo. " +
      "Ma-man est en haut Qui fait du gâ-teau, Pa-pa est en bas Qui fait du cho-co-lat. " +
      "Fais do-do, Co-las mon p'tit frè-re, Fais do-do, t'au-ras du lo-lo.",
    ],
  },
  paroles:
    "Fais dodo, Colas mon p'tit frère,\nFais dodo, t'auras du lolo.\n" +
    "Maman est en haut\nQui fait du gâteau,\nPapa est en bas\nQui fait du chocolat.\n" +
    "Fais dodo, Colas mon p'tit frère,\nFais dodo, t'auras du lolo.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une grande sœur chante près du berceau de son petit frère, la nuit." },
    {
      image: "images/01-fais-dodo.svg",
      description: "La grande sœur berce Colas qui s'endort dans son berceau.",
      texte: "Fais dodo, Colas mon p'tit frère,\nFais dodo, t'auras du lolo.",
    },
    {
      image: "images/02-maman.svg",
      description: "En haut, dans la cuisine, Maman prépare un beau gâteau.",
      texte: "Maman est en haut\nQui fait du gâteau,",
    },
    {
      image: "images/03-papa.svg",
      description: "En bas, Papa prépare du chocolat chaud.",
      texte: "Papa est en bas\nQui fait du chocolat.",
    },
    {
      image: "images/04-endormis.svg",
      description: "Colas dort ; sa grande sœur s'est endormie aussi, avec son ours en peluche.",
      texte: "Fais dodo, Colas mon p'tit frère,\nFais dodo, t'auras du lolo.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
