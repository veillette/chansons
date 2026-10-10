Chansonnier.ajouter({
  id: "le-bon-roi-dagobert",
  titre: "Le bon roi Dagobert",
  sousTitre: "A mis sa culotte à l'envers",
  auteur: "Chanson traditionnelle (XVIIIe siècle)",
  age: "3 à 8 ans",
  genre: "Chanson à rire",
  couleur: "#7048e8",
  vignette: "images/vignette.svg",
  resume:
    "Le bon roi Dagobert est bien distrait : il met sa culotte à l'envers, se fait courser par un lapin " +
    "et part en mer… Heureusement, le grand saint Éloi veille sur lui !",
  melodie: {
    tempo: 112,
    mesure: "6/8",
    anacrouse: 0.5,
    notes:
      "mi4:0.5 | mi4 ré4:0.5 ré4 do4:0.5 | do4:1.5 ré4:1.5 | mi4:0.5 fa4:0.5 mi4:0.5 ré4:0.5 do4:0.5 ré4:0.5 | do4:1.5 -:0.5 do4:0.5 ré4:0.5 | " +
      "mi4 mi4:0.5 mi4:0.5 fa4:0.5 sol4:0.5 | ré4 ré4:0.5 ré4:0.5 do4:0.5 ré4:0.5 | mi4 mi4:0.5 mi4:0.5 fa4:0.5 sol4:0.5 | ré4 ré4:0.5 ré4 mi4:0.5 | " +
      "mi4 ré4:0.5 ré4 do4:0.5 | do4:1.5 ré4:1.5 | mi4:0.5 fa4:0.5 mi4:0.5 ré4:0.5 do4:0.5 ré4:0.5 | do4:2.5",
    syllabes: [
      "Le bon roi Da-go-bert A mis sa cu-lotte à l'en-vers. Le grand saint É-loi Lui dit : « Ô mon roi ! Vo-tre " +
      "Ma-jes-té Est mal cu-lot-tée. » « C'est vrai, lui dit le roi, Je vais la re-mettre à l'en-droit. »",
      "Le bon roi Da-go-bert Chas-sait dans la plai-ne d'An-vers. Le grand saint É-loi Lui dit : « Ô mon roi ! Vo-tre " +
      "Ma-jes-té Est bien es-souf-flée. » « C'est vrai, lui dit le roi, Un la-pin cou-rait a-près moi. »",
      "Le bon roi Da-go-bert Vou-lait s'em-bar-quer sur la mer. Le grand saint É-loi Lui dit : « Ô mon roi ! Vo-tre " +
      "Ma-jes-té Se fe-ra noy-er. » « C'est vrai, lui dit le roi, On pour-ra cri-er : Le roi boit ! »",
    ],
  },
  paroles:
    "Le bon roi Dagobert\nA mis sa culotte à l'envers.\nLe grand saint Éloi\nLui dit : « Ô mon roi !\nVotre Majesté\nEst mal culottée. »\n« C'est vrai, lui dit le roi,\nJe vais la remettre à l'endroit. »\n\n" +
    "Le bon roi Dagobert\nChassait dans la plaine d'Anvers.\nLe grand saint Éloi\nLui dit : « Ô mon roi !\nVotre Majesté\nEst bien essoufflée. »\n« C'est vrai, lui dit le roi,\nUn lapin courait après moi. »\n\n" +
    "Le bon roi Dagobert\nVoulait s'embarquer sur la mer.\nLe grand saint Éloi\nLui dit : « Ô mon roi !\nVotre Majesté\nSe fera noyer. »\n« C'est vrai, lui dit le roi,\nOn pourra crier : Le roi boit ! »",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Devant son château, le roi Dagobert porte sa culotte bleue sur la tête ; saint Éloi, stupéfait, la lui montre du doigt." },
    {
      image: "images/01-a-l-envers.svg",
      description: "Dans sa chambre, le roi, tout fier, a enfilé sa culotte… sur sa tête, par-dessus sa couronne !",
      texte: "Le bon roi Dagobert\nA mis sa culotte à l'envers.",
    },
    {
      image: "images/02-saint-eloi.svg",
      description: "Le moine Éloi, à la grande barbe blanche, montre la culotte au roi, qui grimace.",
      texte: "Le grand saint Éloi\nLui dit : « Ô mon roi !\nVotre Majesté\nEst mal culottée. »",
    },
    {
      image: "images/03-a-l-endroit.svg",
      description: "Le roi rit aux éclats : sa culotte bleue est enfin à sa place.",
      texte: "« C'est vrai, lui dit le roi,\nJe vais la remettre à l'endroit. »",
    },
    {
      image: "images/04-le-lapin.svg",
      description: "Le roi s'enfuit, les bras en l'air, poursuivi par un grand lapin blanc à l'air malin.",
      texte: "Le bon roi Dagobert\nChassait dans la plaine d'Anvers…\n« C'est vrai, lui dit le roi,\nUn lapin courait après moi. »",
    },
    {
      image: "images/05-sur-la-mer.svg",
      description: "Assis dans une barque violette sur la mer, le roi lève sa tasse.",
      texte: "Le bon roi Dagobert\nVoulait s'embarquer sur la mer…\n« C'est vrai, lui dit le roi,\nOn pourra crier : Le roi boit ! »",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
