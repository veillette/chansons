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
    tempo: 126,
    notes:
      "sol4 mi4 sol4 mi4 sol4 la4 sol4:2 | fa4 ré4 fa4 ré4 fa4 sol4 fa4:2 | " +
      "sol4 mi4 sol4 mi4 sol4 la4 sol4:2 | fa4 ré4 si3 ré4 do4:2 - | " +
      "mi4 mi4 fa4 fa4 sol4:2 sol4:2 | fa4 fa4 mi4 ré4 do4:2 -",
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
