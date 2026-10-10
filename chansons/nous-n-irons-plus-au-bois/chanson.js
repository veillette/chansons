Chansonnier.ajouter({
  id: "nous-n-irons-plus-au-bois",
  titre: "Nous n'irons plus au bois",
  sousTitre: "Les lauriers sont coupés",
  auteur: "Chanson traditionnelle (XVIIIe siècle)",
  age: "3 à 8 ans",
  genre: "Ronde",
  couleur: "#2f9e44",
  vignette: "images/vignette.svg",
  resume:
    "Les lauriers du bois sont coupés : la belle va les ramasser. Alors, tous en rond, on entre dans la " +
    "danse, on saute, on danse… et on embrasse qui l'on veut !",
  melodie: {
    tempo: 108,
    mesure: "2/4",
    notes:
      "-:0.5 do4:0.5 mi4:0.5 fa4:0.5 | sol4 do5 | sol4:0.75 la4:0.25 sol4:0.5 fa4:0.5 | mi4 ré4 | " +
      "do4:0.5 do4:0.5 mi4:0.5 fa4:0.5 | sol4 do5 | sol4:0.75 la4:0.25 sol4:0.5 fa4:0.5 | mi4 ré4 | do4 - | " +
      "do4:0.75 do4:0.25 do4:0.5 ré4:0.5 | do4 sol3 | do4:0.75 do4:0.25 do4:0.5 ré4:0.5 | do4 sol3 | " +
      "sol4 mi4 | sol4 mi4 | ré4:0.75 mi4:0.25 fa4:0.5 mi4:0.5 | ré4:0.5 sol4:0.5 do4",
    syllabes: [
      "Nous n'i-rons plus au bois, Les lau-riers sont cou-pés. La bel-le que voi-là I-ra les ra-mas-ser. En-trez dans " +
      "la dan-se, Voy-ez com-me~on dan-se : Sau-tez, dan-sez, Em-bras-sez qui vous vou-drez.",
    ],
  },
  paroles:
    "Nous n'irons plus au bois,\nLes lauriers sont coupés.\nLa belle que voilà\nIra les ramasser.\n\n" +
    "Refrain :\nEntrez dans la danse,\nVoyez comme on danse :\nSautez, dansez,\nEmbrassez qui vous voudrez.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Quatre enfants font la ronde dans une clairière, entre deux souches de lauriers coupés." },
    {
      image: "images/01-les-lauriers.svg",
      description: "Dans le bois, il ne reste que des souches : un petit garçon, étonné, porte les mains à ses joues.",
      texte: "Nous n'irons plus au bois,\nLes lauriers sont coupés.",
    },
    {
      image: "images/02-la-belle.svg",
      description: "Une jeune fille en robe violette, une fleur dans les cheveux, ramasse les branches de laurier.",
      texte: "La belle que voilà\nIra les ramasser.",
    },
    {
      image: "images/03-la-danse.svg",
      refrain: true,
      description: "Les enfants se tiennent par la main et dansent en rond en riant.",
      texte: "Entrez dans la danse,\nVoyez comme on danse :",
    },
    {
      image: "images/04-sautez.svg",
      refrain: true,
      description: "Les enfants sautent, les bras en l'air ; des cœurs s'envolent au-dessus d'eux.",
      texte: "Sautez, dansez,\nEmbrassez qui vous voudrez !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
