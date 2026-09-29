Chansonnier.ajouter({
  id: "au-clair-de-la-lune",
  titre: "Au clair de la lune",
  sousTitre: "Mon ami Pierrot",
  auteur: "Chanson traditionnelle",
  age: "0 à 6 ans",
  genre: "Berceuse",
  couleur: "#364fc7",
  vignette: "images/vignette.svg",
  resume:
    "Sa chandelle est morte : Lubin frappe chez Pierrot pour emprunter une plume. " +
    "Mais Pierrot est déjà au lit ! La plus célèbre des chansons du soir, à fredonner doucement.",
  melodie: {
    tempo: 104,
    notes:
      "do4 do4 do4 ré4 | mi4:2 ré4:2 | do4 mi4 ré4 ré4 | do4:4 | " +
      "do4 do4 do4 ré4 | mi4:2 ré4:2 | do4 mi4 ré4 ré4 | do4:4 | " +
      "ré4 ré4 ré4 ré4 | la3:2 la3:2 | ré4 do4 si3 la3 | sol3:4 | " +
      "do4 do4 do4 ré4 | mi4:2 ré4:2 | do4 mi4 ré4 ré4 | do4:4",
  },
  paroles:
    "Au clair de la lune,\nMon ami Pierrot,\nPrête-moi ta plume\nPour écrire un mot.\nMa chandelle est morte,\nJe n'ai plus de feu ;\nOuvre-moi ta porte\nPour l'amour de Dieu.\n\n" +
    "Au clair de la lune,\nPierrot répondit :\n« Je n'ai pas de plume,\nJe suis dans mon lit.\nVa chez la voisine,\nJe crois qu'elle y est,\nCar dans sa cuisine\nOn bat le briquet. »\n\n" +
    "Au clair de la lune,\nL'aimable Lubin\nFrappe chez la brune ;\nElle répond soudain :\n« Qui frappe de la sorte ? »\nIl dit à son tour :\n« Ouvrez votre porte\nPour le dieu d'Amour. »",

  pages: [
    { type: "couverture", image: "images/couverture.svg", description: "Pierrot, tout de blanc vêtu, chante sous la lune dans une rue endormie." },
    {
      image: "images/01-plume.svg",
      description: "Lubin tient une chandelle éteinte et rêve d'une plume pour écrire.",
      texte: "Au clair de la lune,\nMon ami Pierrot,\nPrête-moi ta plume\nPour écrire un mot.",
    },
    {
      image: "images/02-porte.svg",
      description: "Lubin frappe à la porte de Pierrot : toc, toc !",
      texte: "Ma chandelle est morte,\nJe n'ai plus de feu ;\nOuvre-moi ta porte\nPour l'amour de Dieu.",
    },
    {
      image: "images/03-dans-son-lit.svg",
      description: "Pierrot est couché dans son lit et dort à moitié.",
      texte: "Au clair de la lune,\nPierrot répondit :\n« Je n'ai pas de plume,\nJe suis dans mon lit. »",
    },
    {
      image: "images/04-la-voisine.svg",
      description: "Pierrot montre à Lubin la maison éclairée de la voisine.",
      texte: "« Va chez la voisine,\nJe crois qu'elle y est… »",
    },
    {
      image: "images/05-le-briquet.svg",
      description: "Dans sa cuisine, la voisine allume le feu de la cheminée.",
      texte: "« … Car dans sa cuisine\nOn bat le briquet. »",
    },
    {
      image: "images/06-qui-frappe.svg",
      description: "La voisine ouvre la porte à Lubin, un peu surprise.",
      texte: "Au clair de la lune,\nL'aimable Lubin\nFrappe chez la brune ;\nElle répond soudain :\n« Qui frappe de la sorte ? »",
    },
    {
      image: "images/07-ouvrez.svg",
      description: "Lubin et la voisine sourient ; la chandelle est rallumée.",
      texte: "Il dit à son tour :\n« Ouvrez votre porte\nPour le dieu d'Amour. »",
    },
    { type: "quatrieme", image: "images/vignette.svg" },
  ],
});
