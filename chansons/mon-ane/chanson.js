Chansonnier.ajouter({
  id: "mon-ane",
  titre: "Mon âne, mon âne",
  sousTitre: "Et des souliers lilas, la, la",
  auteur: "Chanson traditionnelle",
  age: "2 à 7 ans",
  genre: "Chanson à accumulation",
  couleur: "#7048e8",
  vignette: "images/vignette.svg",
  resume:
    "Le pauvre âne a mal partout ! Heureusement, Madame lui offre un bonnet, des boucles d'oreilles, des lunettes bleues… " +
    "À chaque couplet, on ajoute un cadeau et on répète tous les autres.",
  melodie: {
    tempo: 112,
    notes:
      "sol4 mi4 sol4 mi4:2 | do4 ré4 mi4 fa4 sol4:2 | la4 sol4 fa4 mi4 ré4:2 | " +
      "fa4 mi4 ré4 do4 ré4:2 | fa4 mi4 ré4 do4 ré4:2 | " +
      "mi4 mi4 fa4 sol4 la4 sol4:0.5 sol4:0.5 | mi4 ré4 do4:2",
  },
  paroles:
    "Mon âne, mon âne\nA bien mal à la tête.\nMadame lui a fait faire\nUn bonnet pour sa fête,\nUn bonnet pour sa fête\n" +
    "Et des souliers lilas, la, la,\nEt des souliers lilas.\n\n" +
    "Mon âne, mon âne\nA bien mal aux oreilles.\nMadame lui a fait faire\nUne paire de boucles d'oreilles,\n" +
    "Une paire de boucles d'oreilles,\nUn bonnet pour sa fête\nEt des souliers lilas, la, la,\nEt des souliers lilas.\n\n" +
    "Mon âne, mon âne\nA bien mal à ses yeux.\nMadame lui a fait faire\nUne paire de lunettes bleues,\n" +
    "Une paire de lunettes bleues,\nUne paire de boucles d'oreilles,\nUn bonnet pour sa fête\n" +
    "Et des souliers lilas, la, la,\nEt des souliers lilas.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un âne gris coiffé d'un bonnet rouge, avec des souliers lilas, à côté d'une vieille dame en violet." },
    {
      image: "images/01-mal-a-la-tete.svg",
      description: "L'âne se tient la tête à deux mains, l'air malheureux.",
      texte: "Mon âne, mon âne\nA bien mal à la tête.",
    },
    {
      image: "images/02-un-bonnet.svg",
      description: "Madame lui a donné un bonnet rouge et des souliers lilas ; l'âne rit, les bras en l'air.",
      texte: "Madame lui a fait faire\nUn bonnet pour sa fête,\nUn bonnet pour sa fête\nEt des souliers lilas, la, la,\nEt des souliers lilas.",
    },
    {
      image: "images/03-mal-aux-oreilles.svg",
      description: "L'âne pleure en se tenant les joues : il a mal aux oreilles.",
      texte: "Mon âne, mon âne\nA bien mal aux oreilles.",
    },
    {
      image: "images/04-boucles-d-oreilles.svg",
      description: "L'âne porte maintenant des boucles d'oreilles dorées qui brillent.",
      texte: "Madame lui a fait faire\nUne paire de boucles d'oreilles,\nUne paire de boucles d'oreilles,\nUn bonnet pour sa fête\nEt des souliers lilas, la, la,\nEt des souliers lilas.",
    },
    {
      image: "images/05-mal-aux-yeux.svg",
      description: "L'âne se couvre les yeux avec ses sabots.",
      texte: "Mon âne, mon âne\nA bien mal à ses yeux.",
    },
    {
      image: "images/06-lunettes-bleues.svg",
      description: "Avec ses lunettes, son bonnet, ses boucles d'oreilles et ses souliers, l'âne est très fier ; Madame danse de joie.",
      texte: "Madame lui a fait faire\nUne paire de lunettes bleues,\nUne paire de lunettes bleues,\nUne paire de boucles d'oreilles,\nUn bonnet pour sa fête\nEt des souliers lilas, la, la,\nEt des souliers lilas !",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
