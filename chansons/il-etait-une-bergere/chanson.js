Chansonnier.ajouter({
  id: "il-etait-une-bergere",
  titre: "Il était une bergère",
  sousTitre: "Et ron, ron, ron, petit patapon",
  auteur: "Chanson traditionnelle",
  age: "3 à 8 ans",
  genre: "Chanson à refrain",
  couleur: "#e64980",
  vignette: "images/vignette.svg",
  resume:
    "La bergère a fait un bon fromage avec le lait de ses moutons. Le chat la regarde d'un petit air " +
    "fripon… « Si tu y mets la patte, gare au bâton ! » Il n'y met pas la patte : il y met le menton !",
  melodie: {
    tempo: 104,
    mesure: "6/8",
    anacrouse: 0.5,
    notes:
      "sol3:0.5 | do4 ré4:0.5 mi4 ré4:0.5 | do4:1.5 sol3 sol3:0.5 | la3 la3:0.5 sol3:0.5 sol3:0.5 sol3:0.5 | la3 la3:0.5 sol3 sol3:0.5 | " +
      "do4 ré4:0.5 mi4 ré4:0.5 | do4:1.5 sol3 sol4:0.5 | mi4 do4:0.5 ré4 si3:0.5 | do4 do4:0.5 do4 sol4:0.5 | mi4 do4:0.5 ré4 si3:0.5 | do4:2.5",
    syllabes: [
      "Il é-tait un' ber-gè-re, Et ron, ron, ron, pe-tit pa-ta-pon, Il é-tait un' ber-gè-re, Qui gar-dait ses " +
      "mou-tons, Ron, ron, Qui gar-dait ses mou-tons.",
      "El-le fit un fro-ma-ge, Et ron, ron, ron, pe-tit pa-ta-pon, El-le fit un fro-ma-ge, Du lait de ses mou-tons, " +
      "Ron, ron, Du lait de ses mou-tons.",
      "Le chat qui la re-gar-de, Et ron, ron, ron, pe-tit pa-ta-pon, Le chat qui la re-gar-de, D'un pe-tit air " +
      "fri-pon, Ron, ron, D'un pe-tit air fri-pon.",
    ],
  },
  paroles:
    "Il était une bergère,\nEt ron, ron, ron, petit patapon,\nIl était une bergère,\nQui gardait ses moutons,\nRon, ron,\nQui gardait ses moutons.\n\n" +
    "Elle fit un fromage,\nEt ron, ron, ron, petit patapon,\nElle fit un fromage,\nDu lait de ses moutons,\nRon, ron,\nDu lait de ses moutons.\n\n" +
    "Le chat qui la regarde,\nEt ron, ron, ron, petit patapon,\nLe chat qui la regarde,\nD'un petit air fripon,\nRon, ron,\nD'un petit air fripon.\n\n" +
    "Si tu y mets la patte,\nEt ron, ron, ron, petit patapon,\nSi tu y mets la patte,\nTu auras du bâton,\nRon, ron,\nTu auras du bâton.\n\n" +
    "Il n'y mit pas la patte,\nEt ron, ron, ron, petit patapon,\nIl n'y mit pas la patte,\nIl y mit le menton,\nRon, ron,\nIl y mit le menton.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une bergère aux longues tresses chante au milieu de ses moutons ; des notes roses s'envolent." },
    {
      image: "images/01-la-bergere.svg",
      description: "La bergère en robe rose sourit au milieu de ses trois moutons blancs.",
      texte: "Il était une bergère,\nEt ron, ron, ron, petit patapon,\nQui gardait ses moutons,\nRon, ron.",
    },
    {
      image: "images/02-le-fromage.svg",
      description: "Dans la cuisine, la bergère montre fièrement le fromage posé sur la table, à côté du pot de lait.",
      texte: "Elle fit un fromage\nDu lait de ses moutons,\nRon, ron.",
    },
    {
      image: "images/03-le-chat.svg",
      description: "Un chat gris regarde le fromage du coin de l'œil, l'air gourmand.",
      texte: "Le chat qui la regarde\nD'un petit air fripon,\nRon, ron.",
    },
    {
      image: "images/04-la-patte.svg",
      description: "La bergère, fâchée, gronde le chat en levant le doigt ; le chat fait la grimace.",
      texte: "« Si tu y mets la patte,\nTu auras du bâton ! »\nRon, ron.",
    },
    {
      image: "images/05-le-menton.svg",
      description: "Le chat est grimpé sur la table, le museau dans le fromage ; la bergère n'en revient pas !",
      texte: "Il n'y mit pas la patte,\nIl y mit le menton !\nRon, ron.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
