Chansonnier.ajouter({
  id: "dans-la-foret-lointaine",
  titre: "Dans la forêt lointaine",
  sousTitre: "Coucou, hibou",
  auteur: "Chanson traditionnelle",
  age: "2 à 7 ans",
  genre: "Chanson en canon",
  couleur: "#5f3dc4",
  vignette: "images/vignette.svg",
  resume:
    "Tout en haut d'un grand chêne, le coucou appelle… et le hibou lui répond ! " +
    "On peut la chanter en canon : un groupe fait le coucou, l'autre le hibou.",
  melodie: {
    tempo: 96,
    mesure: "2/4",
    notes:
      "do4:0.5 mi4:0.5 sol4:0.5 sol4:0.5 | sol4:0.5 sol4:0.5 sol4 | la4:0.5 la4:0.5 sol4:0.5 sol4:0.5 | fa4 mi4 | " +
      "ré4:0.5 fa4:0.5 la4:0.5 la4:0.5 | la4:0.5 la4:0.5 la4 | si4:0.5 si4:0.5 la4:0.5 la4:0.5 | la4 sol4 | " +
      "sol4 mi4 | sol4 mi4 | sol4 mi4 | sol4 mi4 | sol4 mi4 | sol4 mi4 | ré4 do4",
    syllabes: [
      "Dans la fo-rêt loin-tai-ne, On en-tend le cou-cou. " +
      "Du haut de son grand chê-ne, Il ré-pond au hi-bou : " +
      "Cou-cou, hi-bou, cou-cou, hi-bou, Cou-cou, hi-bou, cou-cou.",
    ],
  },
  paroles:
    "Dans la forêt lointaine,\nOn entend le coucou.\nDu haut de son grand chêne,\nIl répond au hibou :\n" +
    "Coucou, hibou, coucou, hibou,\nCoucou, hibou, coucou.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Le soir dans la forêt, un coucou gris et un hibou sont perchés dans un grand chêne sous la lune." },
    {
      image: "images/01-la-foret.svg",
      description: "Une forêt verte ; au loin, un petit oiseau gris vole en criant coucou.",
      texte: "Dans la forêt lointaine,\nOn entend le coucou.",
    },
    {
      image: "images/02-le-coucou.svg",
      description: "Le coucou chante, perché tout en haut d'un grand chêne.",
      texte: "Du haut de son grand chêne,",
    },
    {
      image: "images/03-le-hibou.svg",
      description: "La nuit tombe ; un hibou ouvre l'œil et répond : hou hou !",
      texte: "Il répond au hibou :",
    },
    {
      image: "images/04-coucou-hibou.svg",
      description: "Le coucou et le hibou se répondent de chaque côté du chêne.",
      refrain: true,
      texte: "Coucou, hibou, coucou, hibou,\nCoucou, hibou, coucou.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
