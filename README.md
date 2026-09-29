# Chansons pour enfants 🎵

Un petit site de **chansons enfantines et de berceuses traditionnelles** illustrées :
on les chante en regardant les images, on **écoute l'air**, et on les **imprime**
pour en faire de petits livres, un par chanson, ou un **recueil** qui les regroupe toutes.

- `index.html` : toutes les chansons (couvertures, bouton 🎵 pour écouter l'air).
- `lire.html?chanson=<id>` : feuilleter une chanson (flèches du clavier, glisser du
  doigt, double page sur grand écran, 🎵 jouer l'air, 🔊 lecture à voix haute).
- `lire.html?recueil` : le recueil, avec son sommaire et une page de paroles par chanson.
- `lire.html?partitions` : le livret de partitions, l'air de chaque chanson avec les
  paroles sous les notes.
- `imprimer.html?chanson=<id>`, `imprimer.html?recueil` ou `imprimer.html?partitions` :
  aperçu des feuilles et impression.

Le site est entièrement statique (HTML + CSS + JavaScript, sans étape de
compilation). Seule dépendance : [abcjs](https://github.com/paulrosen/abcjs)
(licence MIT) pour dessiner les partitions, hébergée dans `lib/abcjs/`. Il reprend le moteur du dépôt
[livres](https://github.com/veillette/livres).

Toutes les chansons sont **traditionnelles** ou anciennes (domaine public). Les illustrations
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
| À la claire fontaine | berceuse |
| Une poule sur un mur | comptine |
| Savez-vous planter les choux ? | chanson à gestes |
| Il pleut, il pleut, bergère | chanson douce |
| Pomme de reinette et pomme d'api | comptine à jouer |
| Dans la forêt lointaine | chanson en canon |
| Bateau sur l'eau | jeu de balancement |
| Mon âne, mon âne | chanson à accumulation |
| Il court, il court, le furet | chanson à jouer |
| Ah ! vous dirai-je, maman | comptine |

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
**toutes les chansons du catalogue** avec leurs images, celles du recueil et du
livret de partitions.
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

## Les partitions

Le livret de partitions est construit de la même façon (`chargerPartitions()`
dans `js/chansons.js`) : couverture, sommaire, la partition de chaque chanson,
quatrième de couverture. `js/partition.js` convertit la mélodie en notation ABC
et la fait dessiner par abcjs, avec les couplets empilés sous les notes. Les
barres de mesure sont calculées à partir de la mesure ; une note qui dépasse la
barre est coupée en deux notes liées. Le nombre de mesures par portée dépend de
la place que prennent les syllabes, et une chanson trop longue continue sur la
page suivante.

Ses images sont dans `chansons/partitions/images/`.

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
     melodie: {
       tempo: 100,
       mesure: "4/4",
       notes: "do4 do4 do4 ré4 | mi4:2 ré4:2 | do4 mi4 ré4 ré4 | do4:4",
       syllabes: ["Au clair de la lu-ne, Mon a-mi Pier-rot,"],
     },
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
- `|` (barre de mesure) aide seulement à relire : les barres de la partition
  sont calculées, mais `outils/verifier.py` signale un `|` qui tombe au milieu
  d'une mesure ;
- `tempo` : nombre de temps (noires) par minute (100 par défaut).

Pour la partition :

- `mesure` : `"2/4"`, `"3/4"`, `"4/4"` (par défaut), `"6/8"`… Les durées
  restent comptées en noires : en 6/8, une croche vaut `:0.5` et une mesure
  3 temps ;
- `anacrouse` : nombre de temps avant la première barre de mesure (facultatif) ;
- `syllabes` : un couplet par chaîne, **une syllabe par note** (les silences
  n'en prennent pas). Les mots sont séparés par des espaces et les syllabes d'un
  mot par `-` ; `_` prolonge la syllabe précédente sur une note de plus, `*`
  laisse une note sans paroles, `~` réunit deux mots sous une même note
  (`vi-te~al-lons`). La ponctuation isolée (`Ah !`) reste avec son mot ;
- `mesuresParLigne` (facultatif) : impose le nombre de mesures par portée.

`outils/verifier.py` contrôle la syntaxe de chaque mélodie, que ses `|` tombent
sur des barres de mesure et que le premier couplet a autant de syllabes que de
notes.

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
js/partition.js     partitions (conversion en ABC, dessin par abcjs)
js/bibliotheque.js  page d'accueil
js/lecteur.js       lecteur
js/imposition.js    ordre des pages pour le livret
js/impression.js    page d'impression
js/pwa.js           enregistrement du service worker, bouton « Installer »
sw.js               service worker (cache hors ligne)
manifest.webmanifest, icones/   description de l'application et icônes
polices/            polices Andika et Fredoka (licence OFL), hébergées avec le site
lib/abcjs/          bibliothèque abcjs (licence MIT) qui dessine les partitions
chansons/           un dossier par chanson + catalogue.js + recueil/ + partitions/
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
  berceau, plume et chandelle, notes de musique, fontaine, chaumière, moutons,
  mur de pierres, furet, barque… ;
- `histoires/<id>.py` : les images d'une chanson, une fonction par image
  (`histoires/recueil.py` et `histoires/partitions.py` pour les couvertures du
  recueil et du livret de partitions).

```sh
python3 outils/illustrer/generer.py                 # toutes les chansons
python3 outils/illustrer/generer.py frere-jacques   # une seule chanson
```

Les images sont écrites dans `chansons/<id>/images/`.

Avant chaque publication, GitHub Actions lance `outils/verifier.py`, puis
`generer.py` : si les images produites diffèrent de celles du dépôt, la
publication s'arrête. Seul le site est publié, sans `outils/illustrer/`.
