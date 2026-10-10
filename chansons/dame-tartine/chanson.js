Chansonnier.ajouter({
  id: "dame-tartine",
  titre: "Il était une dame Tartine",
  sousTitre: "Dans un beau palais de beurre frais",
  auteur: "Chanson traditionnelle (XIXe siècle)",
  age: "3 à 8 ans",
  genre: "Comptine gourmande",
  couleur: "#e67700",
  vignette: "images/vignette.svg",
  resume:
    "Dame Tartine habite un palais de beurre frais : les murs sont en praline, le parquet en croquets, et " +
    "dans sa chambre, le lit est fait de biscuits. Un palais à croquer !",
  melodie: {
    tempo: 104,
    mesure: "6/8",
    anacrouse: 1.5,
    notes:
      "do4 mi4:0.5 | sol4 sol4:0.5 fa4:0.5 sol4:0.5 fa4:0.5 | mi4 mi4:0.5 do4 mi4:0.5 | sol4 sol4:0.5 fa4:0.5 sol4:0.5 fa4:0.5 | mi4 -:0.5 do4 mi4:0.5 | " +
      "sol4 sol4:0.5 fa4:0.5 sol4:0.5 fa4:0.5 | mi4 mi4:0.5 do4 mi4:0.5 | sol4 sol4:0.5 fa4:0.5 sol4:0.5 fa4:0.5 | mi4:0.5 -:0.5 mi4:0.5 mi4:0.5 fa4:0.5 ré4:0.5 | " +
      "mi4 mi4:0.5 mi4:0.5 fa4:0.5 ré4:0.5 | mi4 mi4:0.5 mi4:0.5 fa4:0.5 ré4:0.5 | sol4 do4:0.5 ré4:0.5 do4:0.5 si3:0.5 | do4:1.5",
    syllabes: [
      "Il é-tait u-ne da-me Tar-tine Dans un beau pa-lais de beurre frais. La mu-rail-le~é-tait de pra-li-ne, Le " +
      "par-quet é-tait de cro-quets. La cham-bre~à cou-cher De crè-me de lait, Le lit de bis-cuits, Les ri-deaux " +
      "d'a-nis.",
    ],
  },
  paroles:
    "Il était une dame Tartine\nDans un beau palais de beurre frais.\nLa muraille était de praline,\nLe parquet était de croquets.\nLa chambre à coucher\nDe crème de lait,\nLe lit de biscuits,\nLes rideaux d'anis.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Dame Tartine, en robe jaune, brandit une tartine devant son palais couleur de beurre aux toits de praline." },
    {
      image: "images/01-dame-tartine.svg",
      description: "Dame Tartine, un nœud orange dans les cheveux, lève sa tartine en souriant.",
      texte: "Il était une dame Tartine",
    },
    {
      image: "images/02-palais-de-beurre.svg",
      description: "Un beau palais jaune pâle, couleur de beurre frais, aux toits en praline.",
      texte: "Dans un beau palais de beurre frais.",
    },
    {
      image: "images/03-praline.svg",
      description: "Dans la grande salle, les murs sont en praline et le parquet en petits gâteaux secs ; Dame Tartine se lèche les babines.",
      texte: "La muraille était de praline,\nLe parquet était de croquets.",
    },
    {
      image: "images/04-la-chambre.svg",
      description: "La chambre : un lit crème garni de biscuits, et aux fenêtres, des rideaux semés de graines d'anis.",
      texte: "La chambre à coucher\nDe crème de lait,\nLe lit de biscuits,\nLes rideaux d'anis.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
