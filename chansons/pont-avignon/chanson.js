Chansonnier.ajouter({
  id: "pont-avignon",
  titre: "Sur le pont d'Avignon",
  sousTitre: "On y danse tous en rond",
  auteur: "Chanson traditionnelle",
  age: "2 à 8 ans",
  genre: "Ronde",
  couleur: "#e8590c",
  vignette: "images/vignette.svg",
  resume:
    "Sur le vieux pont d'Avignon, tout le monde danse ! Les beaux messieurs saluent, les belles dames font la révérence, " +
    "les musiciens jouent et les soldats défilent. Une ronde pour danser en se tenant la main.",
  melodie: {
    tempo: 112,
    notes:
      "do4:0.5 do4:0.5 do4 ré4:0.5 ré4:0.5 ré4 | mi4:0.5 fa4:0.5 sol4:0.5 do4:0.5 si3:0.5 do4:0.5 ré4:0.5 sol3:0.5 | " +
      "do4:0.5 do4:0.5 do4 ré4:0.5 ré4:0.5 ré4 | mi4:0.5 fa4:0.5 sol4:0.5 do4:0.5 ré4:0.5 si3:0.5 do4",
  },
  paroles:
    "Refrain :\nSur le pont d'Avignon,\nOn y danse, on y danse,\nSur le pont d'Avignon,\nOn y danse tous en rond.\n\n" +
    "Les beaux messieurs font comme ça,\nEt puis encore comme ça.\n\n" +
    "Les belles dames font comme ça,\nEt puis encore comme ça.\n\n" +
    "Les musiciens font comme ça,\nEt puis encore comme ça.\n\n" +
    "Les soldats font comme ça,\nEt puis encore comme ça.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un monsieur et une dame dansent sur le pont d'Avignon, au-dessus du Rhône." },
    {
      image: "images/01-on-y-danse.svg",
      description: "Une ronde d'enfants et de grands danse sur le pont, main dans la main.",
      refrain: true,
      texte: "Sur le pont d'Avignon,\nOn y danse, on y danse,\nSur le pont d'Avignon,\nOn y danse tous en rond.",
    },
    {
      image: "images/02-les-messieurs.svg",
      description: "Deux beaux messieurs en chapeau haut-de-forme saluent.",
      texte: "Les beaux messieurs font comme ça,\nEt puis encore comme ça.",
    },
    {
      image: "images/03-les-dames.svg",
      description: "Deux belles dames en robe longue font la révérence.",
      texte: "Les belles dames font comme ça,\nEt puis encore comme ça.",
    },
    {
      image: "images/04-les-musiciens.svg",
      description: "Un musicien joue de la trompette, l'autre du tambour.",
      texte: "Les musiciens font comme ça,\nEt puis encore comme ça.",
    },
    {
      image: "images/05-les-soldats.svg",
      description: "Trois petits soldats au garde-à-vous font le salut.",
      texte: "Les soldats font comme ça,\nEt puis encore comme ça.",
    },
    {
      image: "images/06-tous-en-rond.svg",
      description: "Tout le monde danse en rond sur le pont, sous le soleil.",
      refrain: true,
      texte: "Sur le pont d'Avignon,\nOn y danse, on y danse,\nSur le pont d'Avignon,\nOn y danse tous en rond !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
