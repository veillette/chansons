Chansonnier.ajouter({
  id: "bateau-sur-l-eau",
  titre: "Bateau sur l'eau",
  sousTitre: "La rivière, la rivière",
  auteur: "Comptine traditionnelle",
  age: "1 à 5 ans",
  genre: "Jeu de balancement",
  couleur: "#1971c2",
  vignette: "images/vignette.svg",
  resume:
    "On se balance à deux, face à face en se tenant les mains, comme un petit bateau sur la rivière… " +
    "jusqu'à ce qu'il chavire, et plouf ! Une comptine à jouer sur les genoux avec les tout-petits.",
  melodie: {
    tempo: 88,
    mesure: "2/4",
    notes:
      "sol4 mi4 | sol4 mi4 | sol4:0.5 la4:0.5 sol4:0.5 mi4:0.5 | sol4:0.5 la4:0.5 sol4:0.5 mi4:0.5 | " +
      "sol4 mi4 | sol4 mi4 | sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 | mi4:0.5 ré4:0.5 do4 | " +
      "mi4:0.5 mi4:0.5 fa4:0.5 fa4:0.5 | sol4:0.5 sol4:0.5 sol4 | la4:0.5 la4:0.5 sol4:0.5 fa4:0.5 | mi4:0.5 mi4:0.5 ré4 | " +
      "do4:0.5 do4 -:0.5 | do5:2",
    syllabes: [
      "Ba-teau sur l'eau, La ri-viè-re, la ri-viè-re, " +
      "Ba-teau sur l'eau, La ri-viè-re~au bord de l'eau. " +
      "Le ba-teau a cha-vi-ré, Et les en-fants sont tom-bés… Dans l'eau ! Plouf !",
    ],
  },
  paroles:
    "Bateau sur l'eau,\nLa rivière, la rivière,\nBateau sur l'eau,\nLa rivière au bord de l'eau.\n\n" +
    "Le bateau a chaviré,\nEt les enfants sont tombés…\nDans l'eau ! Plouf !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Deux enfants joyeux dans une petite barque à voile sur la rivière, entourés de canards." },
    {
      image: "images/01-bateau.svg",
      description: "Les deux enfants chantent, bien assis dans leur barque rouge.",
      texte: "Bateau sur l'eau,\nLa rivière, la rivière,",
    },
    {
      image: "images/02-au-bord-de-l-eau.svg",
      description: "La barque longe la rive fleurie ; une maman canard et son petit nagent à côté.",
      texte: "Bateau sur l'eau,\nLa rivière au bord de l'eau.",
    },
    {
      image: "images/03-chavire.svg",
      description: "La barque penche d'un coup ; les enfants lèvent les bras, surpris : oh !",
      texte: "Le bateau a chaviré,",
    },
    {
      image: "images/04-plouf.svg",
      description: "Les deux enfants sont dans l'eau jusqu'au cou et rient aux éclats : plouf !",
      texte: "Et les enfants sont tombés…\nDans l'eau ! Plouf !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
