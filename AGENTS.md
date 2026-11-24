# Travailler sur Chansons

- Une chanson vit dans `chansons/<id>/chanson.js`, et `chansons/catalogue.js`
  fixe l'ordre du catalogue et du recueil. Conserver les identifiants pour les
  liens de lecture, d'impression et de partage.
- Modifier les scripts d'illustration dans `outils/illustrer/`, puis lancer
  `python3 outils/illustrer/generer.py`. Les SVG générés sont suivis par Git.
  Le README décrit les paroles, les mélodies et les partitions.
- Le site fonctionne depuis le disque sans compilation ni CDN. `_site/`
  est l'artefact de publication. Ajouter les nouveaux scripts d'interface au
  cache `INTERFACE` de `sw.js`.
- Synchronisation à sens unique depuis Livres : éditer `js/copier-lien.js`,
  `js/imposition.js` et `js/navigation-lecture.js` dans Livres, puis recopier
  avec `node tools/sync-site-helpers.mjs --write` depuis le dépôt Origami
  (qui porte le script de sync). Ne pas modifier ces copies seulement ici.
  Garder dans Chansons le rendu des chansons, la voix et les mélodies.
- Avec Node.js 26, Python 3 et rsync, lancer `bash .github/verifier-site.sh`,
  `bash .github/preparer-site.sh` et `node .github/site-smoke.mjs _site --assets-only`.
- Rédiger les textes et les messages de commit en français.
