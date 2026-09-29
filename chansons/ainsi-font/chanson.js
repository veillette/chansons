Chansonnier.ajouter({
  id: "ainsi-font",
  titre: "Ainsi font, font, font",
  sousTitre: "Les petites marionnettes",
  auteur: "Comptine traditionnelle",
  age: "0 à 4 ans",
  genre: "Jeu de doigts",
  couleur: "#c92a2a",
  vignette: "images/vignette.svg",
  resume:
    "Sur la scène du petit théâtre, les marionnettes dansent, font trois petits tours, puis s'en vont. " +
    "Une comptine à mimer avec les mains : on les fait tourner comme des marionnettes, puis on les cache dans son dos.",
  melodie: {
    tempo: 108,
    notes:
      "do4:0.5 mi4:0.5 sol4 sol4 sol4 | sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 mi4:0.5 ré4:0.5 ré4 do4 | " +
      "do4:0.5 mi4:0.5 sol4 sol4 sol4 | sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 mi4 ré4 do4:2",
  },
  paroles:
    "Ainsi font, font, font\nLes petites marionnettes,\nAinsi font, font, font,\nTrois p'tits tours et puis s'en vont.\n\n" +
    "Les mains aux côtés,\nSautez, sautez, marionnettes,\nLes mains aux côtés,\nMarionnettes, recommencez !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une marionnette à fils lève les bras sur la scène d'un petit théâtre." },
    {
      image: "images/01-ainsi-font.svg",
      description: "Trois marionnettes à fils dansent côte à côte sur la scène.",
      texte: "Ainsi font, font, font\nLes petites marionnettes,",
    },
    {
      image: "images/02-trois-p-tits-tours.svg",
      description: "Une marionnette tourne sur elle-même ; une autre fait au revoir en quittant la scène.",
      texte: "Ainsi font, font, font,\nTrois p'tits tours et puis s'en vont.",
    },
    {
      image: "images/03-sautez.svg",
      description: "Les trois marionnettes, les mains sur les hanches, sautent en l'air.",
      texte: "Les mains aux côtés,\nSautez, sautez, marionnettes,",
    },
    {
      image: "images/04-recommencez.svg",
      description: "Une marionnette ouvre grand les bras pour saluer le public.",
      texte: "Les mains aux côtés,\nMarionnettes, recommencez !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
