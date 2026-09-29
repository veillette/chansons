Chansonnier.ajouter({
  id: "meunier-tu-dors",
  titre: "Meunier, tu dors",
  sousTitre: "Ton moulin va trop vite",
  auteur: "Chanson traditionnelle",
  age: "2 à 6 ans",
  genre: "Chanson à gestes",
  couleur: "#d9480f",
  vignette: "images/vignette.svg",
  resume:
    "Le meunier fait la sieste sur ses sacs de farine… et pendant ce temps, le vent se lève ! " +
    "Une chanson à gestes : on fait tourner les bras comme les ailes du moulin, de plus en plus vite.",
  melodie: {
    tempo: 110,
    notes:
      "do4 do4 ré4 mi4:2 | mi4 fa4 sol4 mi4 fa4 sol4 | la4 sol4 fa4:2 | " +
      "do4 do4 ré4 mi4:2 | mi4 fa4 sol4 mi4 fa4 sol4 | fa4 ré4 do4:2 | " +
      "sol4 la4 sol4 fa4 mi4 fa4 | sol4 la4 sol4:2 | sol4 la4 sol4 fa4 mi4 ré4 | mi4 ré4 do4:2",
  },
  paroles:
    "Meunier, tu dors,\nTon moulin, ton moulin va trop vite.\nMeunier, tu dors,\nTon moulin, ton moulin va trop fort.\n" +
    "Ton moulin, ton moulin va trop vite,\nTon moulin, ton moulin va trop fort.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Le meunier dort contre un sac de farine devant son moulin à vent." },
    {
      image: "images/01-tu-dors.svg",
      description: "Le meunier ronfle ; les ailes du moulin tournent vite.",
      texte: "Meunier, tu dors,\nTon moulin, ton moulin\nVa trop vite.",
    },
    {
      image: "images/02-trop-fort.svg",
      description: "Le vent souffle fort ; la farine s'envole de partout, le meunier dort toujours.",
      texte: "Meunier, tu dors,\nTon moulin, ton moulin\nVa trop fort.",
    },
    {
      image: "images/03-reveille-toi.svg",
      description: "Un cochon, un mouton et un lapin crient pour réveiller le meunier.",
      texte: "Ton moulin, ton moulin\nVa trop vite,",
    },
    {
      image: "images/04-oh-la-la.svg",
      description: "Le meunier s'est réveillé d'un coup, les bras en l'air : oh là là !",
      texte: "Ton moulin, ton moulin\nVa trop fort !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
