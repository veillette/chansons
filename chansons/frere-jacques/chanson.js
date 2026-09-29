Chansonnier.ajouter({
  id: "frere-jacques",
  titre: "Frère Jacques",
  sousTitre: "Dormez-vous ?",
  auteur: "Chanson traditionnelle",
  age: "0 à 6 ans",
  genre: "Comptine en canon",
  couleur: "#e8590c",
  vignette: "images/vignette.svg",
  resume:
    "Le matin est arrivé, mais frère Jacques dort encore ! Qui va sonner la cloche ? " +
    "Une chanson toute simple à chanter en canon, à deux, à trois ou à quatre voix.",
  melodie: {
    tempo: 120,
    mesure: "4/4",
    notes:
      "do4 ré4 mi4 do4 | do4 ré4 mi4 do4 | mi4 fa4 sol4:2 | mi4 fa4 sol4:2 | " +
      "sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 mi4 do4 | sol4:0.5 la4:0.5 sol4:0.5 fa4:0.5 mi4 do4 | " +
      "do4 sol3 do4:2 | do4 sol3 do4:2",
    syllabes: [
      "Frè-re Jac-ques, frè-re Jac-ques, Dor-mez-vous ? Dor-mez-vous ? " +
      "Son-nez les ma-ti-nes ! Son-nez les ma-ti-nes ! Ding, daing, dong ! Ding, daing, dong !",
    ],
  },
  paroles:
    "Frère Jacques, frère Jacques,\nDormez-vous ? Dormez-vous ?\nSonnez les matines !\nSonnez les matines !\nDing, daing, dong !\nDing, daing, dong !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Frère Jacques bâille devant le clocher, au lever du soleil." },
    {
      image: "images/01-il-dort.svg",
      description: "Frère Jacques dort à poings fermés dans son petit lit.",
      texte: "Frère Jacques,\nfrère Jacques,",
    },
    {
      image: "images/02-dormez-vous.svg",
      description: "Un vieux moine vient le réveiller : « Dormez-vous ? »",
      texte: "Dormez-vous ?\nDormez-vous ?",
    },
    {
      image: "images/03-le-clocher.svg",
      description: "Le soleil est levé ; le vieux moine montre la cloche du clocher.",
      texte: "Sonnez les matines !\nSonnez les matines !",
    },
    {
      image: "images/04-ding-daing-dong.svg",
      description: "La grosse cloche dorée se balance et sonne.",
      texte: "Ding, daing, dong !\nDing, daing, dong !",
    },
    {
      image: "images/05-reveil.svg",
      description: "Frère Jacques se réveille d'un bond, les bras en l'air.",
      texte: "Oh ! Frère Jacques est réveillé !",
    },
    {
      image: "images/06-en-canon.svg",
      description: "Frère Jacques, un ours, un lapin et un chat chantent l'un après l'autre.",
      texte: "Et maintenant, chantons-la en canon : chacun commence quand le précédent arrive à « Dormez-vous ? ».",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
