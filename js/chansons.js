/*
 * Chansonnier : chargement des chansons et rendu des pages.
 *
 * Chaque chanson vit dans son propre dossier `chansons/<id>/` et contient un
 * fichier `chanson.js` qui appelle `Chansonnier.ajouter({...})`.
 * La liste des chansons affichées se trouve dans `chansons/catalogue.js`.
 *
 * On charge les chansons avec des balises <script> (et non fetch) pour que le
 * site fonctionne aussi en ouvrant simplement index.html depuis le disque.
 *
 * Le recueil (toutes les chansons dans un seul livret) est un « livre
 * virtuel » construit à partir du catalogue : voir `chargerRecueil()`.
 * Le livret de partitions aussi : voir `chargerPartitions()`.
 */
(function () {
  "use strict";

  const chansons = new Map();

  function chargerScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = src;
      script.onload = resolve;
      script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
      document.head.appendChild(script);
    });
  }

  function element(tag, classe, texte) {
    const el = document.createElement(tag);
    if (classe) el.className = classe;
    if (texte != null) el.textContent = texte;
    return el;
  }

  /* Typographie française : espace insécable fine devant ! ? ; : » et après «,
     pour que la ponctuation ne se retrouve jamais seule en début de ligne. */
  function typographie(texte) {
    return texte.replace(/[  ]([!?;:»])/g, " $1").replace(/«[  ]/g, "« ");
  }

  /* Un texte est fait de strophes séparées par une ligne vide ; dans une
     strophe, chaque retour à la ligne commence un nouveau vers. */
  function blocTexte(texte, classe = "page__texte") {
    const bloc = element("div", classe);
    String(texte || "")
      .split(/\n\s*\n/)
      .map((p) => p.trim())
      .filter(Boolean)
      .forEach((strophe) => {
        const p = element("p");
        strophe.split("\n").forEach((vers, i) => {
          if (i > 0) p.appendChild(document.createElement("br"));
          p.appendChild(document.createTextNode(typographie(vers.trim())));
        });
        bloc.appendChild(p);
      });
    return bloc;
  }

  /* Paroles complètes d'une chanson, pour le recueil : le champ `paroles`,
     ou à défaut les textes de ses pages, sans répéter deux fois le même. */
  function parolesCompletes(chanson) {
    if (chanson.paroles) return chanson.paroles;
    const vus = new Set();
    return chanson.pages
      .filter((p) => !p.type || p.type === "illustration")
      .map((p) => p.texte)
      .filter((t) => t && !vus.has(t) && vus.add(t))
      .join("\n\n");
  }

  /* Mise en page des paroles dans le recueil : sur deux colonnes quand tous
     les vers sont courts, sinon sur une seule. Une strophe n'est jamais coupée ;
     si les paroles ne tiennent pas sur une page, elles continuent sur la suivante.
     On compte les lignes affichées : un vers long prend plusieurs lignes. */
  const MISE_EN_PAGE = {
    1: { caracteres: 40, lignes: 20 },
    2: { caracteres: 24, lignes: 40 },
  };

  function colonnes(texte) {
    const vers = texte.split("\n").filter((v) => v.trim());
    return vers.length > 10 && vers.every((v) => v.length <= 30) ? 2 : 1;
  }

  function decouper(texte, nb) {
    const { caracteres, lignes: max } = MISE_EN_PAGE[nb];
    const hauteur = (strophe) => strophe.split("\n").reduce((h, v) => h + Math.max(1, Math.ceil(v.length / caracteres)), 0);
    const pages = [];
    let courante = [];
    let lignes = 0;
    for (const strophe of texte.split(/\n\s*\n/)) {
      const h = hauteur(strophe);
      if (courante.length && lignes + h > max) {
        pages.push(courante.join("\n\n"));
        courante = [];
        lignes = 0;
      }
      courante.push(strophe);
      lignes += h + 1;
    }
    if (courante.length) pages.push(courante.join("\n\n"));
    return pages;
  }

  /* Portées de la partition d'une chanson réparties sur des pages : moins de
     portées par page quand plusieurs couplets s'empilent sous les notes, et
     des pages équilibrées (pas une portée seule sur la dernière). */
  function pagesPartition(melodie) {
    const nb = window.Partition.lignes(melodie);
    const couplets = Math.max(1, window.Partition.couplets(melodie).length);
    const max = Math.max(2, Math.floor(26 / (2.25 + couplets))); // 8 portées, 6 avec 2 couplets, 4 avec 3
    const pages = Math.ceil(nb / max);
    const tranches = [];
    for (let i = 0, debut = 0; i < pages; i++) {
      const fin = debut + Math.ceil((nb - debut) / (pages - i));
      tranches.push([debut, fin]);
      debut = fin;
    }
    return tranches;
  }

  /* Un livret qui regroupe toutes les chansons : couverture, sommaire, pages de
     chaque chanson (construites par `pagesDe`), quatrième de couverture. */
  function livretCatalogue(liste, pagesDe) {
    const pagesChansons = [];
    const entrees = [];
    liste.forEach((c) => {
      const pages = pagesDe(c);
      if (!pages.length) return;
      entrees.push({ titre: c.titre, page: 2 + pagesChansons.length }); // 0 = couverture, 1 = sommaire
      pagesChansons.push(...pages);
    });
    return { entrees, pagesChansons };
  }

  const Chansonnier = {
    ajouter(chanson) {
      if (!chanson || !chanson.id || !chanson.titre || !Array.isArray(chanson.pages) || chanson.pages.length === 0) {
        console.error("Chanson invalide (id, titre et au moins une page sont requis) :", chanson);
        return;
      }
      chansons.set(chanson.id, chanson);
    },

    async charger(id) {
      if (!/^[a-z0-9-]+$/.test(id || "")) {
        throw new Error(`Identifiant de chanson invalide : « ${id} »`);
      }
      if (!chansons.has(id)) await chargerScript(`chansons/${id}/chanson.js`);
      const chanson = chansons.get(id);
      if (!chanson) throw new Error(`Le fichier de la chanson « ${id} » n'a pas appelé Chansonnier.ajouter()`);
      return chanson;
    },

    async chargerTout() {
      const ids = window.CATALOGUE || [];
      const resultats = await Promise.all(
        ids.map((id) =>
          this.charger(id).catch((err) => {
            console.error(err);
            return null;
          })
        )
      );
      return resultats.filter(Boolean);
    },

    /*
     * Le recueil : couverture, sommaire, une page de paroles par chanson
     * (avec sa vignette et sa mélodie), quatrième de couverture.
     * Ses propres images sont dans `chansons/recueil/images/`.
     */
    async chargerRecueil() {
      const liste = await this.chargerTout();
      const { entrees, pagesChansons } = livretCatalogue(liste, (c) => {
        const paroles = parolesCompletes(c);
        const nb = colonnes(paroles);
        return decouper(paroles, nb).map((texte, i) => ({
          type: "paroles",
          chanson: c.id,
          titre: i ? `${c.titre} (suite)` : c.titre,
          texte,
          colonnes: nb,
          image: i ? null : c.vignette,
          description: c.titre,
          couleur: c.couleur,
          melodie: c.melodie,
        }));
      });
      return {
        id: "recueil",
        recueil: true,
        titre: "Mes chansons",
        sousTitre: "Comptines et berceuses",
        auteur: "Chansons traditionnelles",
        age: "0 à 6 ans",
        couleur: "#5f3dc4",
        resume:
          `${liste.length} chansons à chanter, à fredonner et à mimer : ` +
          "des comptines pour jouer, des rondes pour danser et des berceuses pour s'endormir.",
        pages: [
          { type: "couverture", image: "images/couverture.svg", description: "Des enfants et des animaux chantent sous la lune." },
          { type: "sommaire", entrees },
          ...pagesChansons,
          { type: "quatrieme", image: "images/vignette.svg" },
        ],
      };
    },

    /*
     * Le livret de partitions : couverture, sommaire, la partition de chaque
     * chanson (notes et paroles, sur une ou plusieurs pages), quatrième de
     * couverture. Ses propres images sont dans `chansons/partitions/images/`.
     */
    async chargerPartitions() {
      const liste = await this.chargerTout();
      const { entrees, pagesChansons } = livretCatalogue(liste, (c) =>
        !c.melodie
          ? []
          : pagesPartition(c.melodie).map(([debut, fin], i) => ({
              type: "partition",
              chanson: c.id,
              titre: i ? `${c.titre} (suite)` : c.titre,
              image: i ? null : c.vignette,
              description: c.titre,
              couleur: c.couleur,
              melodie: c.melodie,
              debut,
              fin,
            }))
      );
      return {
        id: "partitions",
        partitions: true,
        titre: "Mes partitions",
        sousTitre: "Les notes et les paroles",
        auteur: "Chansons traditionnelles",
        age: "Pour chanter et jouer",
        couleur: "#5f3dc4",
        resume:
          `Les airs des ${liste.length} chansons, avec les paroles sous les notes : ` +
          "pour chanter juste, ou pour les jouer au piano, à la flûte ou au xylophone.",
        pages: [
          { type: "couverture", image: "images/couverture.svg", description: "Une enfant et un oiseau chantent devant une portée de musique." },
          { type: "sommaire", entrees },
          ...pagesChansons,
          { type: "quatrieme", image: "images/vignette.svg" },
        ],
      };
    },

    /* La chanson ou le livret demandé dans l'adresse (?chanson=<id>, ?recueil ou ?partitions). */
    depuisAdresse(params = new URLSearchParams(location.search)) {
      if (params.has("recueil")) return this.chargerRecueil();
      if (params.has("partitions")) return this.chargerPartitions();
      return this.charger(params.get("chanson") || (window.CATALOGUE || [])[0]);
    },

    parametre(chanson) {
      if (chanson.recueil) return "recueil";
      if (chanson.partitions) return "partitions";
      return `chanson=${encodeURIComponent(chanson.id)}`;
    },

    /* Chemin relatif au dossier de la chanson. Pas de chemin absolu (« /… ») :
       il casserait quand le site est publié dans un sous-dossier (GitHub Pages).
       Une page du recueil indique la chanson à laquelle appartient son image. */
    cheminImage(chanson, image, page) {
      if (/^(https?:|data:)/.test(image)) return image;
      return `chansons/${(page && page.chanson) || chanson.id}/${image}`;
    },

    /*
     * Crée l'élément DOM d'une page. Sa taille est donnée par le parent :
     * tout le contenu est dimensionné en unités de conteneur (cqw / cqh),
     * donc la page s'adapte aussi bien à l'écran qu'à la feuille imprimée.
     */
    creerPage(chanson, page, index) {
      const type = page.type || "illustration";
      const el = element("div", `page page--${type}`);
      el.style.setProperty("--couleur", page.couleur || chanson.couleur || "#3a7bd5");
      if (page.fond) el.style.setProperty("--fond", page.fond);
      if (page.refrain) el.classList.add("page--refrain");

      const image = (src, classe = "page__cadre") => {
        const cadre = element("div", classe);
        const img = element("img", "page__image");
        img.src = this.cheminImage(chanson, src, page);
        img.alt = page.description || "";
        img.decoding = "async";
        cadre.appendChild(img);
        return cadre;
      };

      switch (type) {
        case "couverture": {
          if (page.image) el.appendChild(image(page.image));
          const bloc = element("div", "page__titre-bloc");
          const titre = page.titre || chanson.titre;
          const long = titre.length > 22 ? " page__titre--long" : "";
          bloc.appendChild(element("h1", `page__titre${long}`, titre));
          if (chanson.sousTitre) bloc.appendChild(element("p", "page__sous-titre", chanson.sousTitre));
          el.appendChild(bloc);
          if (chanson.auteur) el.appendChild(element("p", "page__auteur", chanson.auteur));
          break;
        }

        case "titre": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          contenu.appendChild(element("h1", "page__titre", chanson.titre));
          if (chanson.sousTitre) contenu.appendChild(element("p", "page__sous-titre", chanson.sousTitre));
          if (page.image) contenu.appendChild(image(page.image, "page__vignette"));
          const credits = element("div", "page__credits");
          if (chanson.auteur) credits.appendChild(element("p", null, `Paroles et musique : ${chanson.auteur}`));
          if (chanson.illustrateur) credits.appendChild(element("p", null, `Illustrations : ${chanson.illustrateur}`));
          contenu.appendChild(credits);
          if (page.texte) contenu.appendChild(blocTexte(page.texte, "page__dedicace"));
          break;
        }

        case "texte": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          if (page.image) contenu.appendChild(image(page.image, "page__vignette"));
          contenu.appendChild(blocTexte(page.texte));
          break;
        }

        case "quatrieme": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          if (page.image) contenu.appendChild(image(page.image, "page__vignette"));
          contenu.appendChild(blocTexte(page.texte || chanson.resume));
          if (chanson.age) {
            const pied = el.appendChild(element("div", "page__pied"));
            pied.appendChild(element("span", "page__age", chanson.age));
          }
          break;
        }

        case "sommaire": {
          const contenu = el.appendChild(element("div", "page__contenu"));
          contenu.appendChild(element("h1", "page__titre", page.titre || "Sommaire"));
          const liste = contenu.appendChild(element("ol", "page__sommaire"));
          if ((page.entrees || []).length > 14) el.classList.add("page--sommaire-long");
          (page.entrees || []).forEach((e) => {
            const li = liste.appendChild(element("li"));
            li.appendChild(element("span", "page__sommaire-titre", e.titre));
            li.appendChild(element("span", "page__sommaire-points"));
            li.appendChild(element("span", "page__sommaire-numero", String(e.page)));
          });
          break;
        }

        case "paroles": {
          // Une chanson entière sur une page : titre, vignette, paroles.
          const entete = el.appendChild(element("div", "page__paroles-entete"));
          if (page.image) entete.appendChild(image(page.image, "page__paroles-vignette"));
          entete.appendChild(element("h2", "page__titre", page.titre));
          const texte = blocTexte(page.texte, "page__texte page__paroles");
          if (page.colonnes === 2) el.classList.add("page--paroles-2col");
          el.appendChild(texte);
          break;
        }

        case "partition": {
          // La partition d'une chanson (ou une partie) : titre, vignette, portées.
          const entete = el.appendChild(element("div", "page__paroles-entete"));
          if (page.image) entete.appendChild(image(page.image, "page__paroles-vignette"));
          const titres = entete.appendChild(element("div", "page__partition-titres"));
          titres.appendChild(element("h2", "page__titre", page.titre));
          if (!page.image) entete.classList.add("page__paroles-entete--suite");
          else titres.appendChild(element("p", "page__partition-credit", "Air traditionnel"));
          const portees = el.appendChild(element("div", "page__partition"));
          portees.setAttribute("role", "img");
          portees.setAttribute("aria-label", `Partition de ${page.titre}`);
          if (window.Partition) window.Partition.dessiner(portees, page.melodie, { debut: page.debut, fin: page.fin });
          break;
        }

        case "vide":
          break;

        default: {
          // "illustration" : une image et un texte, selon une disposition.
          const disposition = page.disposition || "image-haut";
          el.classList.add("page--illustration", `page--${disposition}`);
          if (page.positionTexte === "haut") el.classList.add("page--texte-haut");
          if (page.image) el.appendChild(image(page.image));
          if (page.texte) el.appendChild(blocTexte(page.texte));
        }
      }

      const avecNumero = !["couverture", "titre", "quatrieme", "vide", "sommaire"].includes(type);
      if (avecNumero && chanson.numeros !== false && index != null) {
        el.appendChild(element("span", "page__numero", String(index)));
      }
      return el;
    },

    /* Textes d'une page, pour la lecture à voix haute. */
    texteLisible(chanson, page) {
      switch (page.type) {
        case "couverture":
          return [chanson.titre, chanson.auteur].filter(Boolean).join(". ");
        case "titre":
          return [chanson.titre, chanson.sousTitre].filter(Boolean).join(". ");
        case "quatrieme":
          return page.texte || chanson.resume || "";
        case "sommaire":
          return (page.entrees || []).map((e) => e.titre).join(". ");
        case "paroles":
          return `${page.titre}. ${page.texte || ""}`;
        case "partition":
          return page.titre;
        default:
          return page.texte || "";
      }
    },
  };

  window.Chansonnier = Chansonnier;
})();
