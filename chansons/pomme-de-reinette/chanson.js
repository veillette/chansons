Chansonnier.ajouter({
  id: "pomme-de-reinette",
  titre: "Pomme de reinette et pomme d'api",
  sousTitre: "Tapis, tapis rouge",
  auteur: "Comptine traditionnelle",
  age: "2 à 7 ans",
  genre: "Comptine à jouer",
  couleur: "#e03131",
  vignette: "images/vignette.svg",
  resume:
    "Assis en rond sur le tapis, chacun tend ses poings fermés ; à chaque syllabe, on en touche un… " +
    "Celui qui reçoit le dernier « coup de marteau » cache son poing derrière son dos !",
  melodie: {
    tempo: 116,
    notes:
      "sol4 sol4:0.5 mi4:0.5 sol4 sol4:0.5 mi4:0.5 | sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 mi4:2 | ré4 ré4 mi4 ré4 do4:2 | " +
      "sol4 sol4:0.5 mi4:0.5 sol4 sol4:0.5 mi4:0.5 | sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 mi4:2 | ré4 ré4 mi4 ré4 do4:2 | " +
      "mi4 mi4 fa4 fa4 sol4:2 | la4 la4 sol4 fa4 mi4:2 | ré4 ré4 mi4 ré4 | do4:3",
  },
  paroles:
    "Pomme de reinette et pomme d'api,\nTapis, tapis rouge,\nPomme de reinette et pomme d'api,\nTapis, tapis gris.\n" +
    "Cache ton poing derrière ton dos,\nOu j'te donne un coup d'marteau !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Trois enfants sur un tapis rouge, les poings levés, entre deux pommiers." },
    {
      image: "images/01-les-pommes.svg",
      description: "Un pommier chargé de pommes ; une pomme rouge, la reinette, et une jaune, l'api.",
      texte: "Pomme de reinette\nEt pomme d'api,",
    },
    {
      image: "images/02-tapis-rouge.svg",
      description: "Trois enfants rieurs, assis sur un tapis rouge.",
      texte: "Tapis, tapis rouge,\nPomme de reinette\nEt pomme d'api,",
    },
    {
      image: "images/03-tapis-gris.svg",
      description: "Les mêmes enfants, cette fois sur un tapis gris.",
      texte: "Tapis, tapis gris.",
    },
    {
      image: "images/04-cache-ton-poing.svg",
      description: "Une fillette brandit un maillet en mousse ; son ami rit, les mains sur les hanches.",
      texte: "Cache ton poing\nDerrière ton dos,\nOu j'te donne\nUn coup d'marteau !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
