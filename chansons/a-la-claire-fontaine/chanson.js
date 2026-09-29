Chansonnier.ajouter({
  id: "a-la-claire-fontaine",
  titre: "À la claire fontaine",
  sousTitre: "Un rossignol chantait",
  auteur: "Chanson traditionnelle",
  age: "0 à 8 ans",
  genre: "Berceuse",
  couleur: "#1c7ed6",
  vignette: "images/vignette.svg",
  resume:
    "Une promenade jusqu'à la fontaine, une baignade dans l'eau claire, puis une sieste sous le grand chêne " +
    "où chante un rossignol. Une très vieille chanson, douce comme une berceuse, qu'on chante en France comme au Québec.",
  melodie: {
    tempo: 96,
    notes:
      "do4 do4:0.5 mi4:0.5 mi4 ré4:0.5 mi4:0.5 | ré4:0.5 do4:1.5 do4 do4:0.5 mi4:0.5 | mi4 ré4:0.5 mi4:0.5 mi4:2 | " +
      "mi4 mi4:0.5 ré4:0.5 do4 mi4:0.5 sol4:0.5 | mi4:2 sol4 sol4:0.5 mi4:0.5 | do4 mi4:0.5 ré4:0.5 ré4:2 | " +
      "sol4 sol4:0.5 mi4:0.5 sol4 sol4:0.5 mi4:0.5 | do4:2 do4 mi4:0.5 ré4:0.5 | do4 mi4 ré4:0.5 ré4:0.5 do4:2",
  },
  paroles:
    "À la claire fontaine,\nM'en allant promener,\nJ'ai trouvé l'eau si belle\nQue je m'y suis baignée.\n\n" +
    "Il y a longtemps que je t'aime,\nJamais je ne t'oublierai.\n\n" +
    "Sous les feuilles d'un chêne,\nJe me suis fait sécher.\nSur la plus haute branche,\nUn rossignol chantait.\n\n" +
    "Il y a longtemps que je t'aime,\nJamais je ne t'oublierai.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une fillette aux tresses rousses près d'une fontaine de pierre ; un rossignol chante dans un chêne." },
    {
      image: "images/01-la-fontaine.svg",
      description: "La fillette se promène dans un pré fleuri jusqu'à la fontaine.",
      texte: "À la claire fontaine,\nM'en allant promener,\nJ'ai trouvé l'eau si belle\nQue je m'y suis baignée.",
    },
    {
      image: "images/02-baignee.svg",
      description: "La fillette rit dans l'eau claire et fait des éclaboussures.",
      refrain: true,
      texte: "Il y a longtemps que je t'aime,\nJamais je ne t'oublierai.",
    },
    {
      image: "images/03-sous-le-chene.svg",
      description: "La fillette se repose à l'ombre d'un grand chêne, sa serviette à côté d'elle.",
      texte: "Sous les feuilles d'un chêne,\nJe me suis fait sécher.",
    },
    {
      image: "images/04-le-rossignol.svg",
      description: "Tout en haut d'une branche, un rossignol chante ; des notes s'envolent.",
      texte: "Sur la plus haute branche,\nUn rossignol chantait.",
    },
    {
      image: "images/05-refrain.svg",
      description: "Au coucher du soleil, la fillette chante avec le rossignol.",
      refrain: true,
      texte: "Il y a longtemps que je t'aime,\nJamais je ne t'oublierai.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
