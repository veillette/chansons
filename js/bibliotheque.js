/* Page d'accueil : affiche la couverture de chaque chanson du catalogue. */
(async function () {
  "use strict";

  const etageres = document.getElementById("etageres");

  function carte(chanson) {
    const param = Chansonnier.parametre(chanson);
    const article = document.createElement("article");
    article.className = "carte";

    const lien = document.createElement("a");
    lien.className = "carte__couverture";
    lien.href = `lire.html?${param}`;
    lien.setAttribute("aria-label", `Lire « ${chanson.titre} »`);
    lien.appendChild(Chansonnier.creerPage(chanson, chanson.pages[0], 0));
    article.appendChild(lien);

    const corps = document.createElement("div");
    corps.className = "carte__corps";

    const titre = document.createElement("h2");
    titre.textContent = chanson.titre;
    corps.appendChild(titre);

    const meta = document.createElement("p");
    meta.className = "carte__meta";
    meta.textContent = [chanson.genre, chanson.age, `${chanson.pages.length} pages`].filter(Boolean).join(" · ");
    corps.appendChild(meta);

    const actions = document.createElement("div");
    actions.className = "carte__actions";
    actions.innerHTML = `
      <a class="bouton" href="lire.html?${param}">📖 Lire</a>
      <a class="bouton bouton--secondaire" href="imprimer.html?${param}">🖨️ Imprimer</a>`;

    if (chanson.melodie && Melodie.disponible()) {
      const air = document.createElement("button");
      air.type = "button";
      air.className = "bouton bouton--secondaire carte__air";
      air.textContent = "🎵";
      air.title = air.ariaLabel = `Jouer l'air de « ${chanson.titre} »`;
      air.addEventListener("click", async () => {
        const jouait = air.classList.contains("carte__air--joue");
        Melodie.arreter();
        if (jouait) return;
        etageres.querySelectorAll(".carte__air--joue").forEach((b) => b.classList.remove("carte__air--joue"));
        air.classList.add("carte__air--joue");
        air.textContent = "⏹️";
        await Melodie.jouer(chanson.melodie);
        air.classList.remove("carte__air--joue");
        air.textContent = "🎵";
      });
      actions.appendChild(air);
    }
    corps.appendChild(actions);

    article.appendChild(corps);
    return article;
  }

  const chansons = await Chansonnier.chargerTout();
  etageres.replaceChildren();

  if (chansons.length === 0) {
    etageres.innerHTML = '<p class="message">Aucune chanson pour le moment. Ajoute un dossier dans <code>chansons/</code> et inscris-le dans <code>chansons/catalogue.js</code>.</p>';
    return;
  }

  chansons.forEach((chanson) => etageres.appendChild(carte(chanson)));
})();
