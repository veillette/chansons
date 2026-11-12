# Revue des partitions — 11 octobre 2026

Les 32 chansons du catalogue ont été contrôlées. Le livret produit 47 pages de
partitions. Les contrôles portent sur la notation générée et son accord avec les
mélodies du dépôt ; la comparaison avec des recueils extérieurs est ponctuelle.

## Corrections

| Chanson | Problème corrigé |
| --- | --- |
| Meunier, tu dors | Les notes longues décomposées en notes liées consommaient les syllabes suivantes. |
| En passant par la Lorraine | Une note liée au-delà d'une barre recevait le début du vers suivant. |
| Malbrough s'en va-t-en guerre | La continuation liée de « reviendra » recevait le début de sa répétition. |
| Compère Guilleri | `_,` devenait une prolongation suivie d'une syllabe de ponctuation, décalant les couplets 2 et 3. |
| Il pleut, il pleut, bergère | La ponctuation après `_` devenait une syllabe supplémentaire dans le rendu ABC. |
| Ah ! les crocodiles | « gueul' » omettait le deuxième son de « gueu-le », décalant la fin du second couplet ; celui-ci couvre désormais les 42 notes avant le refrain commun. |

Les continuations ajoutées par le découpage musical reçoivent maintenant `_`
dans les paroles ABC. La ponctuation après un marqueur reste sur la syllabe
chantée. Les notes et les durées des mélodies n'ont pas été modifiées.

## Vérification

- `python3 outils/verifier.py` : 32 chansons, aucune erreur.
- `node outils/tests/moteur.test.js` : 14 tests réussis.
- Les tests relisent les partitions avec la bibliothèque abcjs du site :
  hauteurs, durées, silences, liaisons et position de chaque syllabe de chaque
  couplet. Un test vérifie aussi une liaison à cheval sur deux pages.
- Contrôle dans Chromium des 47 pages, avec la police Andika chargée : aucune
  syllabe chevauchante ni élément musical hors du cadre SVG.

## Références consultées

La [norme ABC, section 5](https://abcnotation.com/wiki/abc:standard:v2.2#lyrics)
confirme que les parties d'une note liée occupent des positions distinctes dans
les paroles et que `_` prolonge une syllabe.

Le [répertoire Galouvielle](https://trillian.mit.edu/~jc/music/abc/mirror/galouvielle.free.fr/enfants/RepertoireEnfants.abc)
confirme les 43 hauteurs de *Jean Petit qui danse* après transposition et les
65 hauteurs de la version retenue de *Meunier, tu dors* (avant les autres
variantes du recueil). Le rythme ternaire de cette dernière est une adaptation.
Les partitions de [Compère Guilleri](https://www.gutenberg.org/files/48878/48878-h/music/06-guilleri.pdf)
et d'[En passant par la Lorraine](https://abcnotation.com/tunePage?a=trillian.mit.edu%2F~jc%2Fmusic%2Fabc%2Fmirror%2Fmusicaviva.com%2Ffrance%2Fen-passant-par%2F0000)
ont également été consultées.

Le [canon de Dans la forêt lointaine publié par Flutetunes](https://www.flutetunes.com/tunes/dans-la-foret-lointaine.pdf)
utilise une autre mélodie que celle du dépôt. Cette différence ne suffit pas à
conclure à une erreur dans une chanson traditionnelle. Cette revue ne certifie
donc pas que les 32 airs correspondent tous à une édition historique déterminée.
