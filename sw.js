/*
 * Service worker : rend le site utilisable hors ligne.
 *
 * À l'installation, on met en cache l'interface puis TOUTES les chansons du
 * catalogue : on lit `chansons/catalogue.js`, puis chaque `chanson.js` pour y
 * trouver les images.
 *
 * L'installation n'a lieu que quand ce fichier change. À la publication,
 * .github/workflows/pages.yml remplace VERSION par le numéro du commit : chaque
 * mise en ligne réinstalle donc tout, et les nouvelles images sont de nouveau
 * disponibles hors ligne. Les fichiers inchangés sont revalidés auprès du
 * serveur (réponse 304), pas re-téléchargés.
 *
 * Stratégies :
 *  - pages, scripts, styles : réseau d'abord (pour voir les nouveautés),
 *    cache si hors ligne ou si le réseau tarde plus de DELAI_RESEAU ;
 *  - images et polices : cache seulement, sans requête réseau quand elles y
 *    sont déjà (elles ne changent qu'avec VERSION, à chaque publication) ;
 *  - sur localhost : toujours le réseau d'abord, pour voir tout de suite les
 *    images régénérées pendant qu'on dessine.
 */
const VERSION = "local"; // remplacé à la publication (pages.yml)
const CACHE = `chansons-${VERSION}`;

const INTERFACE = [
  "./",
  "index.html",
  "lire.html",
  "imprimer.html",
  "manifest.webmanifest",
  "css/site.css",
  "css/pages.css",
  "js/chansons.js",
  "js/melodie.js",
  "js/partition.js",
  "lib/abcjs/abcjs-basic-min.js",
  "js/bibliotheque.js",
  "js/lecteur.js",
  "js/imposition.js",
  "js/impression.js",
  "js/pwa.js",
  "chansons/catalogue.js",
  "icones/icone.svg",
  "icones/icone-192.png",
  "icones/icone-512.png",
  "icones/icone-masquable-512.png",
  "icones/apple-touch-icon.png",
  "polices/andika-400.woff2",
  "polices/andika-700.woff2",
  "polices/fredoka.woff2",
];

const EN_LOCAL = ["localhost", "127.0.0.1", "[::1]"].includes(self.location.hostname);

/* Requête qui revalide le cache HTTP du navigateur (If-None-Match) : un
   fichier inchangé coûte une réponse 304 au lieu d'un nouveau téléchargement. */
const revalider = (url) => new Request(url, { cache: "no-cache" });

async function fichiersDesChansons() {
  const reponse = await fetch("chansons/catalogue.js", { cache: "no-cache" });
  const texte = await reponse.text();
  const liste = texte.match(/CATALOGUE\s*=\s*\[([\s\S]*?)\]/);
  const ids = liste ? [...liste[1].matchAll(/["']([a-z0-9-]+)["']/g)].map((m) => m[1]) : [];

  const fichiers = [];
  await Promise.all(
    ids.map(async (id) => {
      const dossier = `chansons/${id}/`;
      fichiers.push(`${dossier}chanson.js`);
      try {
        const source = await (await fetch(`${dossier}chanson.js`, { cache: "no-cache" })).text();
        for (const m of source.matchAll(/["'](images\/[^"']+)["']/g)) fichiers.push(dossier + m[1]);
      } catch {
        /* chanson introuvable : on l'ignore */
      }
    })
  );
  // Images propres au recueil et au livret de partitions.
  for (const livret of ["recueil", "partitions"]) {
    fichiers.push(`chansons/${livret}/images/couverture.svg`, `chansons/${livret}/images/vignette.svg`);
  }
  return [...new Set(fichiers)];
}

self.addEventListener("install", (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(CACHE);
      await cache.addAll(INTERFACE.map(revalider));
      const chansons = await fichiersDesChansons().catch(() => []);
      // Un fichier manquant ne doit pas faire échouer toute l'installation.
      await Promise.all(chansons.map((url) => cache.add(revalider(url)).catch(() => null)));
      await self.skipWaiting();
    })()
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const noms = await caches.keys();
      await Promise.all(noms.filter((n) => n.startsWith("chansons-") && n !== CACHE).map((n) => caches.delete(n)));
      await self.clients.claim();
    })()
  );
});

/* Pour les pages, la clé de cache ignore les paramètres : lire.html?chanson=a
   et lire.html?chanson=b partagent une seule entrée « lire.html ». */
function cleDeCache(requete) {
  if (requete.mode !== "navigate") return requete;
  const url = new URL(requete.url);
  return url.origin + url.pathname;
}

/* Sur une connexion très lente, on n'attend pas le réseau plus que ce délai si
   une copie est en cache ; la réponse du réseau met quand même le cache à jour. */
const DELAI_RESEAU = 4000;

async function reseauDAbord(requete, event) {
  const cache = await caches.open(CACHE);
  const reseau = fetch(requete).then(async (reponse) => {
    if (reponse.ok) await cache.put(cleDeCache(requete), reponse.clone());
    return reponse;
  });
  event.waitUntil(reseau.catch(() => null));

  async function secours() {
    const enCache = await cache.match(cleDeCache(requete), { ignoreSearch: requete.mode === "navigate" });
    if (enCache) return enCache;
    if (requete.mode === "navigate") return (await cache.match("index.html")) || null;
    return null;
  }

  const attente = new Promise((resolve) => setTimeout(resolve, DELAI_RESEAU)).then(async () => (await secours()) || reseau);
  try {
    attente.catch(() => null); // si le réseau a déjà échoué, personne n'attend plus cette promesse
    return await Promise.race([reseau, attente]);
  } catch (err) {
    const copie = await secours();
    if (copie) return copie;
    throw err;
  }
}

async function cacheDAbord(requete) {
  const cache = await caches.open(CACHE);
  const enCache = await cache.match(requete);
  if (enCache) return enCache;
  const reponse = await fetch(requete);
  if (reponse.ok) await cache.put(requete, reponse.clone());
  return reponse;
}

self.addEventListener("fetch", (event) => {
  const requete = event.request;
  if (requete.method !== "GET") return;
  const url = new URL(requete.url);
  if (url.origin !== self.location.origin) return;

  if (!EN_LOCAL && /\.(svg|png|jpe?g|webp|gif|woff2)$/i.test(url.pathname)) {
    event.respondWith(cacheDAbord(requete));
  } else {
    event.respondWith(reseauDAbord(requete, event));
  }
});
