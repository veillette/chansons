Chansonnier.ajouter({
  id: "dodo-l-enfant-do",
  titre: "Dodo, l'enfant do",
  sousTitre: "L'enfant dormira bientôt",
  auteur: "Berceuse traditionnelle",
  age: "0 à 4 ans",
  genre: "Berceuse",
  couleur: "#6741d9",
  vignette: "images/vignette.svg",
  resume:
    "Dans la grange, une poule blanche prépare un petit coco pour l'enfant qui s'endort. " +
    "La plus simple et la plus ancienne des berceuses, pour bercer les tout-petits.",
  melodie: {
    tempo: 76,
    notes:
      "sol4 mi4 sol4 mi4:2 | fa4 mi4 ré4 mi4 fa4 sol4 mi4:2 | " +
      "sol4 mi4 sol4 mi4:2 | fa4 mi4 ré4 sol3 si3 do4:3",
  },
  paroles:
    "Dodo, l'enfant do,\nL'enfant dormira bien vite.\nDodo, l'enfant do,\nL'enfant dormira bientôt.\n\n" +
    "Une poule blanche\nEst là dans la grange,\nQui va faire un petit coco\nPour l'enfant qui va faire dodo.\n\n" +
    "Dodo, l'enfant do,\nL'enfant dormira bien vite.\nDodo, l'enfant do,\nL'enfant dormira bientôt.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un bébé dort dans son berceau ; une poule blanche veille." },
    {
      image: "images/01-dodo.svg",
      description: "Le bébé s'endort dans son berceau, sous la fenêtre étoilée.",
      texte: "Dodo, l'enfant do,\nL'enfant dormira bien vite.",
    },
    {
      image: "images/02-maman-chante.svg",
      description: "Maman berce doucement le berceau en chantant.",
      texte: "Dodo, l'enfant do,\nL'enfant dormira bientôt.",
    },
    {
      image: "images/03-la-grange.svg",
      description: "Dans la grange rouge, sous la lune, une poule blanche est installée sur la paille.",
      texte: "Une poule blanche\nEst là dans la grange,",
    },
    {
      image: "images/04-le-coco.svg",
      description: "La poule blanche est toute fière : elle a pondu un bel œuf.",
      texte: "Qui va faire un petit coco\nPour l'enfant qui va faire dodo.",
    },
    {
      image: "images/05-bonne-nuit.svg",
      description: "La maison s'endort sous le ciel étoilé.",
      texte: "Dodo, l'enfant do,\nL'enfant dormira bien vite.\nDodo, l'enfant do,\nL'enfant dormira bientôt.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
