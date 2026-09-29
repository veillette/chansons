Chansonnier.ajouter({
  id: "alouette",
  titre: "Alouette",
  sousTitre: "Gentille alouette",
  auteur: "Chanson traditionnelle",
  age: "3 à 8 ans",
  genre: "Chanson à répondre",
  couleur: "#a0693a",
  vignette: "images/vignette.svg",
  resume:
    "La tête, le bec, les yeux, le cou… À chaque couplet, la liste s'allonge et il faut tout se rappeler ! " +
    "Une chanson à répondre, très aimée au Québec et en France : un meneur chante, les autres répètent.",
  melodie: {
    tempo: 112,
    notes:
      "do4 ré4:0.5 mi4:0.5 mi4 mi4 | ré4:0.5 do4:0.5 ré4:0.5 mi4:0.5 do4 sol3 | " +
      "do4 ré4:0.5 mi4:0.5 mi4 mi4 | ré4:0.5 do4:0.5 ré4:0.5 mi4:0.5 do4:2 | " +
      "do4:0.5 do4:0.5 do4:0.5 do4:0.5 do4 ré4:0.5 mi4:0.5 | do4:0.5 do4:0.5 do4:0.5 do4:0.5 do4 ré4:0.5 mi4:0.5 | " +
      "mi4 mi4 | ré4 ré4 | mi4:2 ré4 do4:0.5 sol3:0.5 | do4:3",
  },
  paroles:
    "Refrain :\nAlouette, gentille alouette,\nAlouette, je te plumerai.\n\n" +
    "Je te plumerai la tête (bis)\nEt la tête ! (bis)\nAlouette ! (bis)\nAh !\n\n" +
    "Je te plumerai le bec (bis)\nEt le bec ! (bis)\nEt la tête ! (bis)\nAlouette ! (bis)\nAh !\n\n" +
    "Puis on ajoute, à chaque couplet :\nles yeux, le cou, les ailes, les pattes…\nen répétant toute la liste à rebours.",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Un enfant chante avec une alouette au milieu d'un champ fleuri." },
    {
      image: "images/01-alouette.svg",
      description: "L'enfant chante ; l'alouette, toute ronde, rit.",
      refrain: true,
      texte: "Alouette, gentille alouette,\nAlouette, je te plumerai.",
    },
    {
      image: "images/02-tete.svg",
      description: "Avec une grande plume, l'enfant chatouille le haut de sa tête ; l'alouette rit aux éclats.",
      texte: "Je te plumerai la tête,\nJe te plumerai la tête,\nEt la tête !\nAlouette ! Alouette ! Ah !",
    },
    {
      image: "images/03-bec.svg",
      description: "Avec une grande plume, l'enfant chatouille son bec ; l'alouette rit aux éclats.",
      texte: "Je te plumerai le bec,\nJe te plumerai le bec,\nEt le bec ! Et la tête !\nAlouette ! Alouette ! Ah !",
    },
    {
      image: "images/04-yeux.svg",
      description: "Avec une grande plume, l'enfant chatouille ses yeux ; l'alouette rit aux éclats.",
      texte: "Je te plumerai les yeux,\nJe te plumerai les yeux,\nEt les yeux ! Et le bec !\nEt la tête !\nAlouette ! Alouette ! Ah !",
    },
    {
      image: "images/05-cou.svg",
      description: "Avec une grande plume, l'enfant chatouille son cou ; l'alouette rit aux éclats.",
      texte: "Je te plumerai le cou,\nJe te plumerai le cou,\nEt le cou ! Et les yeux !\nEt le bec ! Et la tête !\nAlouette ! Alouette ! Ah !",
    },
    {
      image: "images/06-ailes.svg",
      description: "Avec une grande plume, l'enfant chatouille ses ailes ; l'alouette rit aux éclats.",
      texte: "Je te plumerai les ailes,\nJe te plumerai les ailes,\nEt les ailes ! Et le cou !\nEt les yeux ! Et le bec !\nEt la tête !\nAlouette ! Alouette ! Ah !",
    },
    {
      image: "images/07-pattes.svg",
      description: "Avec une grande plume, l'enfant chatouille ses pattes ; l'alouette rit aux éclats.",
      texte: "Je te plumerai les pattes,\nJe te plumerai les pattes,\nEt les pattes ! Et les ailes !\nEt le cou ! Et les yeux !\nEt le bec ! Et la tête !\nAlouette ! Alouette ! Ah !",
    },
    {
      image: "images/08-envolee.svg",
      description: "L'alouette s'envole en riant ; l'enfant lui fait au revoir.",
      refrain: true,
      texte: "Alouette, gentille alouette,\nAlouette, je te plumerai.",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
