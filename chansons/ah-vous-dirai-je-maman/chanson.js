Chansonnier.ajouter({
  id: "ah-vous-dirai-je-maman",
  titre: "Ah ! vous dirai-je, maman",
  sousTitre: "Les bonbons valent mieux que la raison",
  auteur: "Chanson traditionnelle",
  age: "2 à 6 ans",
  genre: "Comptine",
  couleur: "#d6336c",
  vignette: "images/vignette.svg",
  resume:
    "Papa voudrait qu'on parle comme une grande personne… mais les bonbons, c'est quand même bien meilleur ! " +
    "Un air que tout le monde connaît, le même que « Brille, brille, petite étoile ».",
  melodie: {
    tempo: 104,
    notes:
      "do4 do4 sol4 sol4 | la4 la4 sol4:2 | fa4 fa4 mi4 mi4 | ré4 ré4 do4:2 | " +
      "sol4 sol4 fa4 fa4 | mi4 mi4 ré4:2 | sol4 sol4 fa4 fa4 | mi4 mi4 ré4:2 | " +
      "do4 do4 sol4 sol4 | la4 la4 sol4:2 | fa4 fa4 mi4 mi4 | ré4 ré4 do4:2",
  },

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Une maman et son enfant, les bras en l'air sous une pluie de bonbons." },
    {
      image: "images/01-maman.svg",
      description: "L'enfant, un peu inquiet, vient parler à sa maman.",
      texte: "Ah ! vous dirai-je, maman,\nCe qui cause mon tourment ?",
    },
    {
      image: "images/02-papa.svg",
      description: "Papa, avec ses lunettes, explique que 1 + 1 = 2 ; l'enfant bâille.",
      texte: "Papa veut que je raisonne\nComme une grande personne.",
    },
    {
      image: "images/03-les-bonbons.svg",
      description: "L'enfant, ravi, tire la langue sous une pluie de bonbons de toutes les couleurs.",
      texte: "Moi, je dis que les bonbons\nValent mieux que la raison !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
