Chansonnier.ajouter({
  id: "ah-les-crocodiles",
  titre: "Ah ! les crocodiles",
  sousTitre: "Sur les bords du Nil",
  auteur: "Chanson traditionnelle",
  age: "3 à 8 ans",
  genre: "Chanson à mimer",
  couleur: "#2f9e44",
  vignette: "images/vignette.svg",
  resume:
    "Un crocodile très fier part en guerre contre les éléphants, en chantant à grosses dents. " +
    "Mais quand un éléphant paraît… plouf ! Une chanson à chanter en ouvrant grand les bras comme une gueule de crocodile.",
  melodie: {
    tempo: 120,
    mesure: "2/4",
    notes:
      "do4 do4:0.75 mi4:0.25 | sol4:1.5 fa4:0.5 | mi4:0.75 ré4:0.25 mi4:0.75 fa4:0.25 | mi4 ré4 | " +
      "ré4 ré4:0.75 mi4:0.25 | ré4:1.5 ré4:0.5 | mi4:0.75 ré4:0.25 mi4:0.75 fa#4:0.25 | sol4:2 | " +
      "do4 do4:0.75 mi4:0.25 | sol4:1.5 fa4:0.5 | mi4:0.75 ré4:0.25 mi4:0.75 fa4:0.25 | mi4 ré4 | " +
      "ré4 ré4:0.75 mi4:0.25 | ré4:1.5 ré4:0.5 | mi4:0.75 ré4:0.25 mi4:0.75 fa#4:0.25 | sol4:2 | " +
      "do4:0.5 mi4:0.5 mi4:0.5 mi4:0.5 | do4:0.5 mi4:0.5 mi4:0.5 mi4:0.5 | do4:0.5 mi4:0.5 mi4:0.5 mi4:0.5 | fa4 ré4 | " +
      "si3:0.5 ré4:0.5 ré4:0.5 ré4:0.5 | si3:0.5 ré4:0.5 ré4:0.5 ré4:0.5 | sol4:0.5 fa4:0.5 mi4:0.5 ré4:0.5 | do4:2",
    syllabes: [
      "Un cro-co-dile, s'en al-lant à la guer-re, Di-sait au r'voir à ses pe-tits en-fants. " +
      "Traî-nant sa queue, sa queue dans la pous-siè-re, Il s'en al-lait com-battre les é-lé-phants. " +
      "Ah ! les cro, cro, cro, les cro, cro, cro, les cro-co-di-les, Sur les bords du Nil, ils sont par-tis, n'en par-lons plus~(bis) !",
      "Il fre-don-nait un' mar-che mi-li-tai-re, Dont il mâ-chait les mots à gros-ses dents. " +
      "Quand il ou-vrait la gueul' tout en-tiè-re, On cro-yait voir ses en-ne-mis de-dans.",
    ],
  },
  paroles:
    "Un crocodile, s'en allant à la guerre,\nDisait au revoir à ses petits enfants.\nTraînant sa queue, sa queue dans la poussière,\nIl s'en allait combattre les éléphants.\n\n" +
    "Refrain :\nAh ! les crocrocro, les crocrocro, les crocodiles\nSur les bords du Nil, ils sont partis, n'en parlons plus. (bis)\n\n" +
    "Il fredonnait une marche militaire\nDont il mâchait les mots à grosses dents.\nQuand il ouvrait la gueule tout entière,\nOn croyait voir ses ennemis dedans.\n\n" +
    "Il agitait sa grand' queue à l'arrière,\nComme s'il était d'avance triomphant.\nLes animaux devant sa mine altière\nDans les forêts s'enfuyaient tout tremblants.\n\n" +
    "Un éléphant parut, et sur la terre\nSe prépara ce combat de géants.\nMais près de là courait une rivière :\nLe crocodile s'y jeta subitement.\n\n" +
    "Et tout rempli d'une crainte salutaire,\nS'en retourna vers ses petits enfants.\nNotre éléphant, d'une trompe plus fière,\nVoulut alors accompagner ce chant.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un crocodile coiffé d'un chapeau de papier marche au tambour au bord du Nil." },
    {
      image: "images/01-au-revoir.svg",
      description: "Le crocodile, chapeau sur la tête, dit au revoir à ses trois petits qui pleurent.",
      texte: "Un crocodile, s'en allant à la guerre,\nDisait au revoir à ses petits enfants.",
    },
    {
      image: "images/02-la-poussiere.svg",
      description: "Le crocodile avance fièrement en soulevant la poussière ; un éléphant au loin.",
      texte: "Traînant sa queue, sa queue dans la poussière,\nIl s'en allait combattre les éléphants.",
    },
    {
      image: "images/03-refrain.svg",
      description: "Trois crocodiles nagent dans le fleuve en chantant.",
      refrain: true,
      texte: "Ah ! les crocrocro, les crocrocro, les crocodiles\nSur les bords du Nil, ils sont partis, n'en parlons plus.",
    },
    {
      image: "images/04-marche-militaire.svg",
      description: "Le crocodile joue du tambour et chante une marche.",
      texte: "Il fredonnait une marche militaire\nDont il mâchait les mots à grosses dents.",
    },
    {
      image: "images/05-la-gueule.svg",
      description: "Le crocodile ouvre une immense gueule pleine de dents ; deux oiseaux s'enfuient.",
      texte: "Quand il ouvrait la gueule tout entière,\nOn croyait voir ses ennemis dedans.",
    },
    {
      image: "images/06-tout-tremblants.svg",
      description: "Un lièvre, un lion et une chèvre s'enfuient dans la forêt devant le crocodile.",
      texte: "Il agitait sa grand' queue à l'arrière,\nComme s'il était d'avance triomphant.\nLes animaux devant sa mine altière\nDans les forêts s'enfuyaient tout tremblants.",
    },
    {
      image: "images/07-l-elephant.svg",
      description: "Un énorme éléphant fâché se dresse devant le petit crocodile surpris.",
      texte: "Un éléphant parut, et sur la terre\nSe prépara ce combat de géants.",
    },
    {
      image: "images/08-la-riviere.svg",
      description: "Plouf ! Le crocodile a plongé : on ne voit plus que son œil et son chapeau qui flotte. L'éléphant rit.",
      texte: "Mais près de là courait une rivière :\nLe crocodile s'y jeta subitement.",
    },
    {
      image: "images/09-le-retour.svg",
      description: "Le crocodile est rentré auprès de ses petits ; l'éléphant chante avec eux.",
      texte: "Et tout rempli d'une crainte salutaire,\nS'en retourna vers ses petits enfants.\nNotre éléphant, d'une trompe plus fière,\nVoulut alors accompagner ce chant :",
    },
    {
      image: "images/10-refrain-fin.svg",
      description: "Au coucher du soleil, les crocodiles s'en vont en nageant.",
      refrain: true,
      texte: "Ah ! les crocrocro, les crocrocro, les crocodiles\nSur les bords du Nil, ils sont partis, n'en parlons plus !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
