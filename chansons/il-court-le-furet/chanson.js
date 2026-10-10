Chansonnier.ajouter({
  id: "il-court-le-furet",
  titre: "Il court, il court, le furet",
  sousTitre: "Le furet du bois joli",
  auteur: "Chanson traditionnelle",
  age: "3 à 8 ans",
  genre: "Chanson à jouer",
  couleur: "#a0693a",
  vignette: "images/vignette.svg",
  resume:
    "Les enfants font la ronde en tenant une ficelle où glisse un anneau : c'est le furet ! " +
    "Il passe de main en main pendant la chanson… et celui qui est au milieu doit deviner où il se cache.",
  melodie: {
    tempo: 112,
    mesure: "2/4",
    notes:
      "-:0.5 sol3:0.5 do4:0.5 ré4:0.5 | mi4 ré4:0.5 ré4:0.5 | la3 do4:0.5 si3:0.5 | la3:0.5 sol3:0.5 la3:0.5 si3:0.5 | do4:0.5 sol3:0.5 do4:0.5 ré4:0.5 | mi4 ré4:0.5 ré4:0.5 | la3 do4:0.5 si3:0.5 | la3:0.5 sol3:0.5 la3:0.5 si3:0.5 | " +
      "do4 do4:0.5 si3:0.5 | la3:0.5 sol3:0.5 la3:0.5 si3:0.5 | do4 do4:0.5 si3:0.5 | la3:0.5 sol3:0.5 la3:0.5 si3:0.5 | do4:2",
    syllabes: [
      "Il court, il court, le fu-ret, Le fu-ret du bois, mes-dames, " +
      "Il court, il court, le fu-ret, Le fu-ret du bois jo-li. " +
      "Il est pas-sé par i-ci, Il re-pas-se-ra par là.",
    ],
  },
  paroles:
    "Il court, il court, le furet,\nLe furet du bois, mesdames,\nIl court, il court, le furet,\nLe furet du bois joli.\n\n" +
    "Il est passé par ici,\nIl repassera par là.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Quatre enfants font la ronde dans le bois ; un furet file à toute vitesse devant eux." },
    {
      image: "images/01-il-court.svg",
      description: "Un furet au museau masqué court à toute allure entre les arbres.",
      texte: "Il court, il court, le furet,\nLe furet du bois, mesdames,",
    },
    {
      image: "images/02-la-ronde.svg",
      description: "Les enfants chantent en ronde ; un anneau doré glisse sur la ficelle qu'ils tiennent.",
      texte: "Il court, il court, le furet,\nLe furet du bois joli.",
    },
    {
      image: "images/03-par-ici.svg",
      description: "Le furet sort d'un buisson avec un air malin ; une fillette le montre du doigt.",
      texte: "Il est passé par ici,",
    },
    {
      image: "images/04-par-la.svg",
      description: "Le furet repart dans l'autre sens ; un garçon rit en le montrant.",
      texte: "Il repassera par là !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
