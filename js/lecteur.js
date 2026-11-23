/* Lecteur : feuilleter une chanson (ou le recueil) page par page (ou en double page sur grand écran). */
(async function () {
  "use strict";

  const scene = document.getElementById("scene");
  const position = document.getElementById("position");
  const precedent = document.getElementById("precedent");
  const suivant = document.getElementById("suivant");
  const boutonCopier = document.getElementById("copier-lien");
  const boutonVoix = document.getElementById("voix");
  const boutonAir = document.getElementById("air");

  let chanson;
  try {
    chanson = await Chansonnier.depuisAdresse();
  } catch (err) {
    scene.innerHTML = "";
    const p = document.createElement("p");
    p.className = "message message--erreur";
    p.textContent = err.message;
    scene.appendChild(p);
    precedent.disabled = suivant.disabled = true;
    return;
  }

  document.title = chanson.titre;
  document.getElementById("titre").textContent = chanson.titre;
  document.getElementById("imprimer").href = `imprimer.html?${Chansonnier.parametre(chanson)}`;

  const navigation = NavigationLecture.installer({
    elements: { scene, position, precedent, suivant, boutonCopier },
    pages: chanson.pages,
    adresse: `lire.html?${Chansonnier.parametre(chanson)}`,
    creerPage: (page, i) => Chansonnier.creerPage(chanson, page, i),
    cheminImage: (page) => Chansonnier.cheminImage(chanson, page.image, page),
    avantAffichage: () => {
      arreterVoix();
      arreterAir();
    },
    apresAffichage: () => {
      boutonAir.hidden = !Melodie.disponible() || !melodieCourante();
    },
  });

  // Lecture à voix haute (si le navigateur la propose).
  const synthese = window.speechSynthesis;
  function arreterVoix() {
    if (synthese && synthese.speaking) synthese.cancel();
    boutonVoix.textContent = "🔊 Écouter";
  }

  if (synthese && "SpeechSynthesisUtterance" in window) {
    boutonVoix.hidden = false;
    boutonVoix.addEventListener("click", () => {
      if (synthese.speaking) {
        arreterVoix();
        return;
      }
      arreterAir();
      const texte = navigation.pagesCourantes().map((page) => Chansonnier.texteLisible(chanson, page)).filter(Boolean).join(" ");
      if (!texte) return;
      const phrase = new SpeechSynthesisUtterance(texte);
      phrase.lang = chanson.langue || "fr-FR";
      phrase.rate = 0.9;
      const voix = synthese.getVoices().find((v) => v.lang && v.lang.startsWith("fr"));
      if (voix) phrase.voice = voix;
      phrase.onend = () => (boutonVoix.textContent = "🔊 Écouter");
      boutonVoix.textContent = "⏹️ Arrêter";
      synthese.speak(phrase);
    });
  }

  // Jouer l'air de la chanson.
  function melodieCourante() {
    const page = navigation.pagesCourantes().find((p) => p.melodie);
    return page ? page.melodie : chanson.melodie;
  }

  function arreterAir() {
    Melodie.arreter();
    boutonAir.textContent = "🎵 Jouer l'air";
  }

  boutonAir.addEventListener("click", async () => {
    if (Melodie.joue()) {
      arreterAir();
      return;
    }
    arreterVoix();
    boutonAir.textContent = "⏹️ Arrêter l'air";
    await Melodie.jouer(melodieCourante());
    if (!Melodie.joue()) boutonAir.textContent = "🎵 Jouer l'air";
  });

  window.addEventListener("pagehide", arreterAir);

  navigation.afficher();
})();
