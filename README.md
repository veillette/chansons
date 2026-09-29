# Chansons pour enfants 🎵

Un petit site de **chansons enfantines et de berceuses traditionnelles** illustrées :
on les chante en regardant les images, on **écoute l'air**, et on les **imprime**
pour en faire de petits livres, un par chanson, ou un **recueil** qui les regroupe toutes.

- `index.html` : toutes les chansons (couvertures, bouton 🎵 pour écouter l'air).
- `lire.html?chanson=<id>` : feuilleter une chanson (flèches du clavier, glisser du
  doigt, double page sur grand écran, 🎵 jouer l'air, 🔊 lecture à voix haute).
- `lire.html?recueil` : le recueil, avec son sommaire et une page de paroles par chanson.
- `imprimer.html?chanson=<id>` ou `imprimer.html?recueil` : aperçu des feuilles et impression.

Le site est entièrement statique (HTML + CSS + JavaScript, sans dépendance ni
étape de compilation). Il reprend le moteur du dépôt
[livres](https://github.com/veillette/livres).

Toutes les chansons sont **traditionnelles** (domaine public). Les illustrations
sont dessinées par programme (voir plus bas).

## Les chansons

| Chanson | Genre |
| --- | --- |
| Au clair de la lune | berceuse |
| Frère Jacques | comptine en canon |
| Ah ! les crocodiles | chanson à mimer |
| Une souris verte | comptine |
| Fais dodo | berceuse |
| Alouette | chanson à répondre |
| Il était un petit navire | chanson de marins |
| Sur le pont d'Avignon | ronde |
| Promenons-nous dans les bois | comptine à jouer |
| Ainsi font, font, font | jeu de doigts |
| Meunier, tu dors | chanson à gestes |
| Dodo, l'enfant do | berceuse |

## Voir le site

- **Sur l'ordinateur** : ouvrir `index.html` dans le navigateur, tout simplement.
- **Avec un petit serveur** (recommandé) : `python3 -m http.server`, puis
  <http://localhost:8000>.
- **En ligne** : le fichier `.github/workflows/pages.yml` publie le site sur
  GitHub Pages à chaque poussée sur `main` (*Settings → Pages → Build and
  deployment → Source : GitHub Actions*).

## Application installable (PWA)

Une fois le site en ligne (https), on peut l'**installer** comme une application
sur tablette, téléphone ou ordinateur : bouton « 📲 Installer l'application » sur
l'accueil (Chrome, Edge, Android), ou *Partager → Sur l'écran d'accueil* sur
iPhone / iPad.

Au premier chargement, le service worker (`sw.js`) enregistre l'interface,
**toutes les chansons du catalogue** avec leurs images, et celles du recueil.
Tout fonctionne ensuite **hors ligne**, mélodies et impression comprises.

**Après l'ajout d'une chanson ou la modification d'images**, augmenter `VERSION`
en haut de `sw.js` (`"v1"` → `"v2"`) pour que tout soit de nouveau disponible
hors ligne.

## Imprimer

| Mise en page | Feuille | Résultat |
| --- | --- | --- |
| **Livret à plier** | à l'italienne, 2 pages par face, recto verso | on empile, on plie en deux, on agrafe au milieu |
| **Une page par feuille** | à la française, 1 page par feuille | à relier (spirale, attaches, classeur) |

Papier Lettre (8½ × 11) ou A4. Pour le livret, les pages sont réordonnées
automatiquement et des pages blanches sont ajoutées avant la quatrième de
couverture si le nombre de pages n'est pas un multiple de 4.

Dans la fenêtre d'impression du navigateur : échelle **100 %**, marges **Aucune**,
cocher **Graphiques d'arrière-plan**, et pour le livret **recto verso,
retournement sur le bord court**.

## Le recueil

Le recueil est construit automatiquement à partir du catalogue
(`chargerRecueil()` dans `js/chansons.js`) : couverture, sommaire, paroles
complètes de chaque chanson avec sa vignette, quatrième de couverture. Les
paroles sont mises sur deux colonnes quand tous les vers sont courts ; une
chanson trop longue continue sur la page suivante, sans couper une strophe.
Sur une page du recueil, le bouton 🎵 joue l'air de la chanson affichée.

Les images propres au recueil sont dans `chansons/recueil/images/`.

## Ajouter une chanson

1. Créer un dossier `chansons/ma-chanson/` (lettres minuscules, chiffres et tirets).
2. Y mettre les images dans `chansons/ma-chanson/images/`.
3. Créer `chansons/ma-chanson/chanson.js` :

   ```js
   Chansonnier.ajouter({
     id: "ma-chanson",               // identique au nom du dossier
     titre: "Ma chanson",
     sousTitre: "Facultatif",
     auteur: "Chanson traditionnelle",
     age: "2 à 6 ans",
     genre: "Comptine",               // affiché sur l'accueil
     couleur: "#e8590c",              // couleur de la chanson (couverture, titres)
     vignette: "images/vignette.svg", // petite image utilisée dans le recueil
     resume: "Texte de la quatrième de couverture.",
     melodie: { tempo: 100, notes: "do4 do4 do4 ré4 | mi4:2 ré4:2 | do4 mi4 ré4 ré4 | do4:4" },
     paroles: "Paroles complètes pour le recueil (facultatif).",
     pages: [
       { type: "couverture", image: "images/couverture.svg" },
       { image: "images/01.svg", texte: "Premier vers,\nDeuxième vers." },
       { image: "images/02.svg", refrain: true, texte: "Le refrain…" },
       { type: "quatrieme", image: "images/vignette.svg" },
     ],
   });
   ```

4. Ajouter `"ma-chanson"` dans `chansons/catalogue.js`.
5. Augmenter `VERSION` dans `sw.js`.
6. Lancer `python3 outils/verifier.py` (la publication échoue si cette
   vérification trouve une erreur).

### Paroles

- Dans un `texte`, un retour à la ligne (`\n`) commence un nouveau vers et une
  ligne vide (`\n\n`) sépare deux strophes.
- `refrain: true` sur une page affiche le texte en italique, dans la couleur de
  la chanson.
- `paroles` (facultatif) donne le texte complet affiché dans le recueil, par
  exemple avec des « (bis) » pour gagner de la place. Sans ce champ, le recueil
  reprend les textes des pages, sans les répéter.

### Mélodie

Le champ `melodie` est joué par le navigateur (Web Audio, son de boîte à musique),
sans aucun fichier audio :

- une note : `do ré mi fa sol la si`, puis `#` (dièse) ou `b` (bémol)
  facultatif, puis l'octave (`4` = octave du do du milieu, par défaut) ;
- `:durée` en temps : `:0.5` croche, `:2` blanche, `:1.5` noire pointée
  (par défaut 1) ;
- `-` est un silence (`-:2` = deux temps) ;
- `|` (barre de mesure) est ignorée, elle aide seulement à relire ;
- `tempo` : nombre de temps par minute (100 par défaut).

`outils/verifier.py` contrôle la syntaxe de chaque mélodie.

### Types de pages

Les mêmes que dans [livres](https://github.com/veillette/livres) — `couverture`,
`titre`, `illustration` (par défaut), `texte`, `quatrieme`, `vide` — et, pour le
recueil, `sommaire` et `paroles`. Les pages `illustration` acceptent
`disposition: "image-haut" | "image-bas" | "pleine-page"`.

## Organisation du code

```
index.html, lire.html, imprimer.html
css/site.css        interface du site + règles d'impression
css/pages.css       apparence des pages (en unités cqw/cqh : même rendu écran/papier)
js/chansons.js      chargement des chansons, construction du recueil, rendu d'une page
js/melodie.js       lecture des mélodies (Web Audio)
js/bibliotheque.js  page d'accueil
js/lecteur.js       lecteur
js/imposition.js    ordre des pages pour le livret
js/impression.js    page d'impression
js/pwa.js           enregistrement du service worker, bouton « Installer »
sw.js               service worker (cache hors ligne)
manifest.webmanifest, icones/   description de l'application et icônes
polices/            polices Andika et Fredoka (licence OFL), hébergées avec le site
chansons/           un dossier par chanson + catalogue.js + recueil/
outils/verifier.py  vérification des chansons, des mélodies et des images
outils/illustrer/   dessin des illustrations en SVG
```

## Dessiner les illustrations

Les illustrations sont générées en SVG par un petit outil Python, sans aucune
dépendance, dans `outils/illustrer/` (repris de *livres*) :

- `base.py`, `objets.py`, `fantastique.py`, `contes.py`, `fables.py`,
  `sciences.py` : décors, personnages animaux et humains, accessoires ;
- `chansons.py` : ce qui est propre aux chansons — crocodile, alouette, petit
  navire, pont d'Avignon, clocher et cloche, moulin à vent, marionnette,
  berceau, plume et chandelle, notes de musique… ;
- `histoires/<id>.py` : les images d'une chanson, une fonction par image
  (`histoires/recueil.py` pour la couverture du recueil).

```sh
python3 outils/illustrer/generer.py                 # toutes les chansons
python3 outils/illustrer/generer.py frere-jacques   # une seule chanson
```

Les images sont écrites dans `chansons/<id>/images/`.

Avant chaque publication, GitHub Actions lance `outils/verifier.py`, puis
`generer.py` : si les images produites diffèrent de celles du dépôt, la
publication s'arrête. Seul le site est publié, sans `outils/illustrer/`.
