Chansonnier.ajouter({
  id: "une-souris-verte",
  titre: "Une souris verte",
  sousTitre: "Qui courait dans l'herbe",
  auteur: "Comptine traditionnelle",
  age: "2 à 6 ans",
  genre: "Comptine",
  couleur: "#2b8a3e",
  vignette: "images/vignette.svg",
  resume:
    "On l'attrape par la queue, on la trempe dans l'huile, on la met dans un tiroir… " +
    "Mais la petite souris verte a toujours le dernier mot ! Une comptine rigolote pour jouer et pour compter.",
  melodie: {
    tempo: 96,
    mesure: "2/4",
    notes:
      "do4:0.5 do4:0.5 mi4:0.5 sol4:0.5 | sol4 sol4 | sol4:0.5 sol4:0.5 mi4:0.5 do4:0.5 | do4 do4 | " +
      "fa4:0.5 fa4:0.5 fa4:0.5 fa4:0.5 | mi4:0.5 mi4:0.5 mi4 | ré4:0.5 ré4:0.5 ré4:0.5 ré4:0.5 | do4:0.5 do4:0.5 do4 | " +
      "sol4:0.5 sol4:0.5 sol4 | mi4:0.5 mi4:0.5 mi4 | sol4:0.5 sol4:0.5 sol4:0.5 sol4:0.5 | mi4 mi4 | " +
      "fa4:0.5 fa4:0.5 fa4:0.5 fa4:0.5 | ré4:2 | ré4:0.5 mi4:0.5 fa4:0.5 mi4:0.5 | ré4 do4 | mi4 do4",
    syllabes: [
      "U-ne sou-ris ver-te Qui cou-rait dans l'her-be, " +
      "Je l'at-tra-pe par la queue, Je la mon-tre~à ces mes-sieurs. " +
      "Ces mes-sieurs me di-sent : « Trem-pez-la dans l'hui-le, " +
      "Trem-pez-la dans l'eau, Ça fe-ra~un es-car-got Tout chaud. »",
    ],
  },
  paroles:
    "Une souris verte\nQui courait dans l'herbe,\nJe l'attrape par la queue,\nJe la montre à ces messieurs.\n" +
    "Ces messieurs me disent :\n« Trempez-la dans l'huile,\nTrempez-la dans l'eau,\nÇa fera un escargot\nTout chaud. »\n\n" +
    "Je la mets dans un tiroir,\nElle me dit : « Il fait trop noir ! »\nJe la mets dans mon chapeau,\nElle me dit : « Il fait trop chaud ! »\n" +
    "Je la mets dans ma culotte,\nElle me fait trois petites crottes !",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une souris verte fait coucou au milieu des fleurs." },
    {
      image: "images/01-dans-l-herbe.svg",
      description: "La souris verte court dans l'herbe, près d'une coccinelle et d'un papillon.",
      texte: "Une souris verte\nQui courait dans l'herbe,",
    },
    {
      image: "images/02-par-la-queue.svg",
      description: "Une enfant tient la souris par la queue et la montre à deux messieurs.",
      texte: "Je l'attrape par la queue,\nJe la montre à ces messieurs.",
    },
    {
      image: "images/03-escargot.svg",
      description: "Un monsieur à chapeau haut-de-forme montre une poêle d'huile et un bol d'eau ; à côté, un escargot vert tout fumant.",
      texte: "Ces messieurs me disent :\n« Trempez-la dans l'huile,\nTrempez-la dans l'eau,\nÇa fera un escargot\nTout chaud. »",
    },
    {
      image: "images/04-tiroir.svg",
      description: "Dans le tiroir ouvert d'une commode, on ne voit que deux petits yeux dans le noir.",
      texte: "Je la mets dans un tiroir,\nElle me dit : « Il fait trop noir ! »",
    },
    {
      image: "images/05-chapeau.svg",
      description: "La souris sort la tête d'un chapeau haut-de-forme ; elle a très chaud sous le soleil.",
      texte: "Je la mets dans mon chapeau,\nElle me dit : « Il fait trop chaud ! »",
    },
    {
      image: "images/06-culotte.svg",
      description: "L'enfant lève les bras, étonnée ; la souris s'enfuit en riant, laissant trois petites crottes.",
      texte: "Je la mets dans ma culotte,\nElle me fait trois petites crottes !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
