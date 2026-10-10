Chansonnier.ajouter({
  id: "cadet-rousselle",
  titre: "Cadet Rousselle",
  sousTitre: "Est bon enfant !",
  auteur: "Chanson traditionnelle (1792)",
  age: "3 à 8 ans",
  genre: "Chanson à rire",
  couleur: "#d9480f",
  vignette: "images/vignette.svg",
  resume:
    "Cadet Rousselle a trois maisons sans toit, trois habits dont un en papier, et trois beaux chats qui " +
    "n'attrapent jamais les rats. Un drôle de bonhomme… mais vraiment, il est bon enfant !",
  melodie: {
    tempo: 120,
    mesure: "6/8",
    anacrouse: 1.5,
    notes:
      "sol3:0.5 la3:0.5 si3:0.5 | do4 do4:0.5 do4 mi4:0.5 | do4:1.5 ré4:0.5 ré4:0.5 ré4:0.5 | ré4 do4:0.5 si3 la3:0.5 | sol3:1.5 sol3:0.5 la3:0.5 si3:0.5 | " +
      "do4 do4:0.5 do4 mi4:0.5 | do4:1.5 ré4:0.5 ré4:0.5 ré4:0.5 | ré4 do4:0.5 si3 la3:0.5 | sol3:1.5 ré4:0.5 ré4:0.5 ré4:0.5 | " +
      "ré4 mi4:0.5 fa4 mi4:0.5 | mi4 ré4:0.5 ré4:0.5 ré4:0.5 ré4:0.5 | ré4 mi4:0.5 fa4 mi4:0.5 | mi4 ré4:0.5 do4:1.5 | " +
      "do4:1.5 do4:0.5 si3:0.5 la3:0.5 | sol3:1.5 do4:0.5 si3:0.5 do4:0.5 | ré4 ré4:0.5 do4 si3:0.5 | do4:1.5",
    syllabes: [
      "Ca-det Rous-selle a trois mai-sons, Ca-det Rous-selle a trois mai-sons, Qui n'ont ni pou-tres ni che-vrons, " +
      "Qui n'ont ni pou-tres ni che-vrons. C'est pour lo-ger les hi-ron-del-les ; Que di-rez-vous d'Ca-det " +
      "Rous-sel-le ? Ah ! ah ! ah ! mais vrai-ment, Ca-det Rous-selle est bon en-fant !",
      "Ca-det Rous-selle a trois ha-bits, Ca-det Rous-selle a trois ha-bits, Deux jau-nes, l'au-tre~en pa-pier gris, " +
      "Deux jau-nes, l'au-tre~en pa-pier gris. Il met ce-lui-là quand il gè-le, Ou quand il pleut, ou quand il " +
      "grê-le. Ah ! ah ! ah ! mais vrai-ment, Ca-det Rous-selle est bon en-fant !",
      "Ca-det Rous-selle a trois beaux chats, Ca-det Rous-selle a trois beaux chats, Qui n'at-tra-pent ja-mais les " +
      "rats, Qui n'at-tra-pent ja-mais les rats. Le troi-sième n'a pas de pru-nel-le, Il mon-te~au gre-nier sans " +
      "chan-del-le. Ah ! ah ! ah ! mais vrai-ment, Ca-det Rous-selle est bon en-fant !",
    ],
  },
  paroles:
    "Cadet Rousselle a trois maisons (bis)\nQui n'ont ni poutres ni chevrons (bis)\nC'est pour loger les hirondelles,\nQue direz-vous d'Cadet Rousselle ?\n\n" +
    "Refrain :\nAh ! Ah ! Ah ! mais vraiment,\nCadet Rousselle est bon enfant !\n\n" +
    "Cadet Rousselle a trois habits (bis)\nDeux jaunes, l'autre en papier gris (bis)\nIl met celui-là quand il gèle,\nOu quand il pleut, ou quand il grêle.\n\n" +
    "Cadet Rousselle a trois beaux chats (bis)\nQui n'attrapent jamais les rats (bis)\nLe troisième n'a pas de prunelle,\nIl monte au grenier sans chandelle.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Cadet Rousselle, ses cheveux roux en bataille, rit devant ses trois maisons sans toit ; des hirondelles volent au-dessus." },
    {
      image: "images/01-trois-maisons.svg",
      description: "Cadet Rousselle montre fièrement ses trois maisons : une, deux, trois.",
      texte: "Cadet Rousselle a trois maisons,\nQui n'ont ni poutres ni chevrons.",
    },
    {
      image: "images/02-les-hirondelles.svg",
      description: "Sans toit, la maison est pleine de nids : les petites hirondelles y ont trouvé un abri.",
      texte: "C'est pour loger les hirondelles,\nQue direz-vous d'Cadet Rousselle ?",
    },
    {
      image: "images/03-bon-enfant.svg",
      refrain: true,
      description: "Cadet Rousselle éclate de rire, les bras en l'air : « Ah ! Ah ! Ah ! »",
      texte: "Ah ! Ah ! Ah ! mais vraiment,\nCadet Rousselle est bon enfant !",
    },
    {
      image: "images/04-trois-habits.svg",
      description: "Sur la corde à linge sèchent deux chemises jaunes et une chemise en papier gris.",
      texte: "Cadet Rousselle a trois habits,\nDeux jaunes, l'autre en papier gris.\nIl met celui-là quand il gèle,\nOu quand il pleut, ou quand il grêle.",
    },
    {
      image: "images/05-trois-chats.svg",
      description: "Deux chats sommeillent à côté d'une souris qui rit ; le troisième grimpe l'échelle du grenier.",
      texte: "Cadet Rousselle a trois beaux chats,\nQui n'attrapent jamais les rats.\nLe troisième n'a pas de prunelle,\nIl monte au grenier sans chandelle.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
