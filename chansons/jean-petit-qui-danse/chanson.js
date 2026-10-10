Chansonnier.ajouter({
  id: "jean-petit-qui-danse",
  titre: "Jean Petit qui danse",
  sousTitre: "De son doigt, doigt, doigt",
  auteur: "Chanson traditionnelle",
  age: "2 à 6 ans",
  genre: "Chanson à gestes",
  couleur: "#f76707",
  vignette: "images/vignette.svg",
  resume:
    "Jean Petit danse du doigt, puis du pied, puis du genou… À chaque couplet, on ajoute une partie du " +
    "corps et on danse avec lui. Qui arrivera à tout faire en même temps ?",
  melodie: {
    tempo: 112,
    mesure: "2/4",
    anacrouse: 1,
    notes:
      "mi4:0.5 si4:0.5 | si4:0.5 la4:0.5 si4 | sol4 la4:0.5 la4:0.5 | si4:0.5 la4:0.5 sol4:0.5 fa#4:0.5 | mi4 mi4:0.5 si4:0.5 | " +
      "si4:0.5 la4:0.5 si4 | sol4 la4:0.5 la4:0.5 | si4:0.5 la4:0.5 sol4:0.5 fa#4:0.5 | mi4 mi4:0.5 fa#4:0.5 | " +
      "sol4 fa#4 | mi4 mi4:0.5 fa#4:0.5 | sol4 la4 | si4 si4:0.75 do5:0.25 | si4:0.5 la4:0.5 sol4:0.5 fa#4:0.5 | mi4",
    syllabes: [
      "Jean Pe-tit qui dan-se, Jean Pe-tit qui dan _ se, De son doigt il dan-se, De son doigt il dan _ se, De son " +
      "doigt, doigt, doigt, De son doigt, doigt, doigt, Ain-si dan-se Jean Pe-tit !",
      "Jean Pe-tit qui dan-se, Jean Pe-tit qui dan _ se, De son pied il dan-se, De son pied il dan _ se, De son pied, " +
      "pied, pied, De son doigt, doigt, doigt, Ain-si dan-se Jean Pe-tit !",
    ],
  },
  paroles:
    "Jean Petit qui danse (bis)\nDe son doigt il danse (bis)\nDe son doigt, doigt, doigt (bis)\nAinsi danse Jean Petit !\n\n" +
    "Jean Petit qui danse (bis)\nDe son pied il danse (bis)\nDe son pied, pied, pied,\nDe son doigt, doigt, doigt,\nAinsi danse Jean Petit !\n\n" +
    "Et l'on continue avec le genou, la main, le coude, la tête…\nen reprenant chaque fois toute la liste !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Jean Petit, en habit orange, danse sous une guirlande de lampions ; des notes s'envolent autour de lui." },
    {
      image: "images/01-jean-petit.svg",
      description: "Jean Petit danse en chantant, les bras grands ouverts.",
      texte: "Jean Petit qui danse,\nJean Petit qui danse,",
    },
    {
      image: "images/02-le-doigt.svg",
      description: "Jean Petit lève un doigt bien haut et le fait danser.",
      texte: "De son doigt il danse,\nDe son doigt, doigt, doigt,\nAinsi danse Jean Petit !",
    },
    {
      image: "images/03-le-pied.svg",
      description: "Jean Petit sautille sur un pied en riant.",
      texte: "De son pied il danse,\nDe son pied, pied, pied,\nDe son doigt, doigt, doigt,\nAinsi danse Jean Petit !",
    },
    {
      image: "images/04-tous-ensemble.svg",
      description: "Les amis de Jean Petit le rejoignent : tout le monde danse, les bras en l'air.",
      texte: "Et maintenant, à vous ! Du genou, de la main, de la tête… Ainsi danse Jean Petit !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
