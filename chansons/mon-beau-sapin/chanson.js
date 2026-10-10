Chansonnier.ajouter({
  id: "mon-beau-sapin",
  titre: "Mon beau sapin",
  sousTitre: "Roi des forêts",
  auteur: "Chant traditionnel, sur l'air allemand « O Tannenbaum »",
  age: "2 à 8 ans",
  genre: "Chant de Noël",
  couleur: "#2b8a3e",
  vignette: "images/vignette.svg",
  resume:
    "L'hiver, les arbres perdent leurs feuilles, mais le sapin, lui, reste tout vert. À Noël, il entre " +
    "dans la maison, couvert de lumières, de bonbons et de jouets.",
  melodie: {
    tempo: 96,
    mesure: "3/4",
    anacrouse: 1,
    notes:
      "sol3 | do4:0.75 do4:0.25 do4 ré4 | mi4:0.75 mi4:0.25 mi4:1.5 mi4:0.5 | ré4:0.5 mi4:0.5 fa4 si3 | ré4 do4 -:0.5 sol4:0.5 | " +
      "sol4:0.5 mi4:0.5 la4:1.5 sol4:0.5 | sol4:0.5 fa4:0.5 fa4:1.5 fa4:0.5 | fa4:0.5 ré4:0.5 sol4:1.5 fa4:0.5 | fa4:0.5 mi4:0.5 mi4 sol3 | " +
      "do4:0.75 do4:0.25 do4 ré4 | mi4:0.75 mi4:0.25 mi4:1.5 mi4:0.5 | ré4:0.5 mi4:0.5 fa4 si3 | ré4 do4",
    syllabes: [
      "Mon beau sa-pin, roi des fo-rêts, Que j'ai-me ta ver-du-re ! Quand par l'hi-ver, bois et gué-rets Sont " +
      "dé-pouil-lés de leurs at-traits, Mon beau sa-pin, roi des fo-rêts, Tu gar-des ta pa-ru-re.",
      "Toi que No-ël plan-ta chez nous Au saint an-ni-ver-sai-re ! Jo-li sa-pin, com-me~ils sont doux Et tes bon-bons " +
      "et tes jou-joux ! Toi que No-ël plan-ta chez nous Tout bril-lant de lu-miè-re.",
      "Mon beau sa-pin, tes verts som-mets Et leur fi-dè-le~om-bra-ge, De la foi qui ne ment ja-mais, De la " +
      "cons-tan-ce~et de la paix, Mon beau sa-pin, tes verts som-mets M'of-frent la dou-ce~i-ma-ge.",
    ],
  },
  paroles:
    "Mon beau sapin, roi des forêts,\nQue j'aime ta verdure !\nQuand par l'hiver, bois et guérets\nSont dépouillés de leurs attraits,\nMon beau sapin, roi des forêts,\nTu gardes ta parure.\n\n" +
    "Toi que Noël planta chez nous\nAu saint anniversaire !\nJoli sapin, comme ils sont doux\nEt tes bonbons et tes joujoux !\nToi que Noël planta chez nous\nTout brillant de lumière.\n\n" +
    "Mon beau sapin, tes verts sommets\nEt leur fidèle ombrage,\nDe la foi qui ne ment jamais,\nDe la constance et de la paix,\nMon beau sapin, tes verts sommets\nM'offrent la douce image.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un grand sapin enneigé, une étoile dorée au-dessus de lui, entre deux petits sapins ; il neige." },
    {
      image: "images/01-roi-des-forets.svg",
      description: "Au milieu des petits sapins de la forêt, le plus grand ; deux enfants l'admirent.",
      texte: "Mon beau sapin, roi des forêts,\nQue j'aime ta verdure !",
    },
    {
      image: "images/02-l-hiver.svg",
      description: "L'hiver : sous la neige, les arbres n'ont plus une feuille, mais le sapin est tout vert.",
      texte: "Quand par l'hiver, bois et guérets\nSont dépouillés de leurs attraits,",
    },
    {
      image: "images/03-ta-parure.svg",
      description: "Le soleil brille sur le grand sapin couvert de neige.",
      texte: "Mon beau sapin, roi des forêts,\nTu gardes ta parure.",
    },
    {
      image: "images/04-noel.svg",
      description: "Dans la maison, le sapin décoré de boules, de bougies et d'une étoile ; des cadeaux et un cheval à bascule au pied.",
      texte: "Toi que Noël planta chez nous\nAu saint anniversaire !\nJoli sapin, comme ils sont doux\nEt tes bonbons et tes joujoux !",
    },
    {
      image: "images/05-tes-verts-sommets.svg",
      description: "La nuit, sous les étoiles, le sapin enneigé et une grande étoile qui brille au-dessus.",
      texte: "Mon beau sapin, tes verts sommets\nEt leur fidèle ombrage,\nDe la foi qui ne ment jamais,\nDe la constance et de la paix…",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
