Chansonnier.ajouter({
  id: "une-poule-sur-un-mur",
  titre: "Une poule sur un mur",
  sousTitre: "Picoti, picota",
  auteur: "Comptine traditionnelle",
  age: "1 à 5 ans",
  genre: "Comptine",
  couleur: "#e8590c",
  vignette: "images/vignette.svg",
  resume:
    "Perchée sur son mur, une poule picore du pain dur… picoti, picota ! " +
    "Une toute petite comptine pour compter qui commence au jeu, ou simplement pour rire.",
  melodie: {
    tempo: 120,
    notes:
      "sol4 sol4 mi4 mi4 | sol4 sol4 mi4:2 | sol4 sol4 mi4 mi4 | sol4 sol4 mi4:2 | " +
      "sol4 la4 sol4 fa4 | mi4 ré4 mi4:2 | fa4 fa4 ré4:2 | mi4 ré4 do4:2",
  },
  paroles: "Une poule sur un mur\nQui picore du pain dur,\nPicoti, picota,\nLève la queue\nEt puis s'en va !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une poule rousse est perchée sur un mur de pierres, à côté d'un morceau de pain." },
    {
      image: "images/01-sur-un-mur.svg",
      description: "La poule, bien droite sur son mur de pierres.",
      texte: "Une poule sur un mur",
    },
    {
      image: "images/02-pain-dur.svg",
      description: "La poule se penche pour picorer un croûton de pain ; des miettes tombent.",
      texte: "Qui picore du pain dur,",
    },
    {
      image: "images/03-picoti.svg",
      description: "Trois poules picorent à tour de rôle : picoti ! picota !",
      texte: "Picoti, picota,",
    },
    {
      image: "images/04-s-en-va.svg",
      description: "La poule, très fière, lève la queue et s'en va.",
      texte: "Lève la queue\nEt puis s'en va !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
