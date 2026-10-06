"""Vérifie les chansons (champs requis, mélodie) et leurs images, y compris hors catalogue.

    python3 outils/verifier.py

Python et Node suffisent ; aucune dépendance à installer.
"""
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

RACINE = Path(__file__).resolve().parents[1]
INVENTAIRE = r"""
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = process.argv[1];
const context = {window: {}};
vm.runInNewContext(fs.readFileSync(path.join(root, 'chansons/catalogue.js'), 'utf8'), context);
const books = [];
for (const folder of fs.readdirSync(path.join(root, 'chansons')).sort()) {
  const filename = path.join(root, 'chansons', folder, 'chanson.js');
  if (!fs.existsSync(filename)) continue;
  vm.runInNewContext(fs.readFileSync(filename, 'utf8'), {
    Chansonnier: {ajouter(book) {books.push({...book, folder});}}
  }, {filename, timeout: 1000});
}
process.stdout.write(JSON.stringify({catalogue: context.window.CATALOGUE, books}));
"""


TYPES = {"couverture", "titre", "illustration", "texte", "quatrieme", "vide"}
# Même notation que js/melodie.js.
NOTE = re.compile(r"(do|r[eé]|mi|fa|sol|la|si)(#|b)?(\d)?(:\d+(\.\d+)?)?")
SILENCE = re.compile(r"-(:\d+(\.\d+)?)?")
DISPOSITIONS = {"image-haut", "image-bas", "pleine-page"}
POSITIONS_TEXTE = {"haut", "bas"}
PONCTUATION = re.compile(r"[!?;:,.»…]+")


def erreurs_structure(chanson):
    """Champs requis par js/chansons.js pour afficher la chanson sans planter."""
    erreurs = []
    if not re.fullmatch(r"[a-z0-9-]+", str(chanson.get("id") or "")):
        erreurs.append("identifiant absent ou invalide (minuscules, chiffres et tirets).")
    if not isinstance(chanson.get("titre"), str) or not chanson["titre"].strip():
        erreurs.append("titre absent.")
    pages = chanson.get("pages")
    if not isinstance(pages, list) or not pages:
        erreurs.append("aucune page.")
        return erreurs
    for numero, page in enumerate(pages):
        if not isinstance(page, dict):
            erreurs.append(f"page {numero} : n'est pas un objet.")
            continue
        type_ = page.get("type", "illustration")
        if type_ not in TYPES:
            erreurs.append(f"page {numero} : type inconnu « {type_} ».")
        if "disposition" in page and page["disposition"] not in DISPOSITIONS:
            erreurs.append(f"page {numero} : disposition inconnue « {page['disposition']} ».")
        if "positionTexte" in page and page["positionTexte"] not in POSITIONS_TEXTE:
            erreurs.append(f"page {numero} : positionTexte inconnue « {page['positionTexte']} ».")
        image = page.get("image")
        if image is not None and (not isinstance(image, str) or image.startswith("/")):
            erreurs.append(f"page {numero} : image invalide ({image!r}) ; utiliser un chemin relatif à la chanson.")
    if not isinstance(chanson.get("vignette"), str):
        erreurs.append("vignette absente (image utilisée dans le recueil).")
    melodie = chanson.get("melodie")
    if melodie is not None:
        if not isinstance(melodie, dict) or not isinstance(melodie.get("notes"), str):
            erreurs.append("melodie : objet { tempo, notes } attendu.")
        else:
            jetons = [j for j in melodie["notes"].split() if j != "|"]
            if not jetons:
                erreurs.append("melodie : aucune note.")
            for jeton in jetons:
                if not (NOTE.fullmatch(jeton) or SILENCE.fullmatch(jeton)):
                    erreurs.append(f"melodie : note inconnue « {jeton} ».")
            tempo = melodie.get("tempo", 100)
            if not isinstance(tempo, (int, float)) or not 20 <= tempo <= 300:
                erreurs.append(f"melodie : tempo invalide ({tempo!r}).")
            if not erreurs:
                erreurs.extend(erreurs_partition(melodie))
    return erreurs


def syllabes(couplet):
    """Syllabes d'un couplet, comptées comme dans js/partition.js."""
    unites = []
    for mot in couplet.split():
        if PONCTUATION.fullmatch(mot) and unites:
            continue  # rattachée à la syllabe précédente
        if mot == "«":
            continue  # rattaché à la syllabe suivante
        unites.extend([mot] if mot in ("_", "*") else [p for p in mot.split("-") if p])
    return unites


def erreurs_partition(melodie):
    """Mesure, anacrouse et syllabes : la partition (js/partition.js) doit tomber juste."""
    erreurs = []
    mesure = re.fullmatch(r"(\d+)/(\d+)", str(melodie.get("mesure", "4/4")))
    if not mesure or mesure[2] not in ("2", "4", "8"):
        return [f"melodie : mesure invalide ({melodie.get('mesure')!r}) ; par exemple \"3/4\" ou \"6/8\"."]
    barre = int(mesure[1]) * 4 / int(mesure[2])  # en temps (noires)
    anacrouse = melodie.get("anacrouse", 0)
    if not isinstance(anacrouse, (int, float)) or not 0 <= anacrouse < barre:
        return [f"melodie : anacrouse invalide ({anacrouse!r})."]
    # Les « | » écrits dans les notes doivent tomber sur les barres calculées.
    position, notes = 0.0, 0
    for jeton in melodie["notes"].split():
        if jeton == "|":
            reste = (position - anacrouse) % barre if position >= anacrouse else anacrouse - position
            if position and min(reste, barre - reste) > 1e-6:
                erreurs.append(f"melodie : barre « | » au milieu d'une mesure (après {position:g} temps).")
            continue
        duree = float(jeton.split(":")[1]) if ":" in jeton else 1.0
        # js/partition.js n'écrit que des durées multiples de la double croche.
        if duree <= 0 or abs(duree * 4 - round(duree * 4)) > 1e-6:
            erreurs.append(f"melodie : durée « {jeton} » impossible à écrire (multiple de 0.25 attendu).")
        position += duree
        notes += not jeton.startswith("-")
    # La dernière mesure complète l'anacrouse : toute la mélodie fait un nombre entier de mesures.
    reste = position % barre
    if min(reste, barre - reste) > 1e-6:
        manque = barre - anacrouse if anacrouse else barre
        erreurs.append(
            f"melodie : {position:g} temps en tout, pas un nombre entier de mesures de {barre:g} temps "
            f"(la dernière mesure doit faire {manque:g} temps)."
        )
    for numero, couplet in enumerate(melodie.get("syllabes") or []):
        if not isinstance(couplet, str):
            erreurs.append(f"melodie : couplet {numero + 1} des syllabes invalide.")
        elif len(syllabes(couplet)) > notes:
            erreurs.append(f"melodie : couplet {numero + 1} : {len(syllabes(couplet))} syllabes pour {notes} notes.")
        elif numero == 0 and len(syllabes(couplet)) != notes:
            erreurs.append(f"melodie : couplet 1 : {len(syllabes(couplet))} syllabes pour {notes} notes.")
    return erreurs


def erreurs_hors_ligne():
    """Les scripts, styles et icônes des pages HTML doivent être dans INTERFACE (sw.js)."""
    source = (RACINE / "sw.js").read_text(encoding="utf-8")
    bloc = re.search(r"const INTERFACE = \[(.*?)\];", source, re.S)
    if not bloc:
        return ["sw.js : liste INTERFACE introuvable."]
    interface = set(re.findall(r'"([^"]+)"', bloc[1]))
    erreurs = []
    for page in sorted(RACINE.glob("*.html")):
        if page.name not in interface:
            erreurs.append(f"sw.js : {page.name} absente de INTERFACE.")
        html = page.read_text(encoding="utf-8")
        for chemin in re.findall(r'<(?:script|link)\b[^>]*?\b(?:src|href)="([^"#?:]+)"', html):
            if chemin not in interface:
                erreurs.append(f"sw.js : {chemin} (utilisé par {page.name}) absent de INTERFACE : la page ne marcherait pas hors ligne.")
    for chemin in sorted(interface - {"./"}):
        if not (RACINE / chemin).is_file():
            erreurs.append(f"sw.js : {chemin} listé dans INTERFACE mais introuvable.")
    return erreurs


def verifier():
    resultat = subprocess.run(
        ["node", "-e", INVENTAIRE, str(RACINE)],
        capture_output=True, text=True, check=True,
    )
    inventaire = json.loads(resultat.stdout)
    erreurs = []
    catalogue = inventaire["catalogue"]
    chansons = inventaire["books"]
    ids = [chanson["id"] for chanson in chansons]
    if len(catalogue) != len(set(catalogue)):
        erreurs.append("Identifiant répété dans le catalogue.")
    if len(ids) != len(set(ids)):
        erreurs.append("Identifiant de chanson répété.")
    for identifiant in set(catalogue) - set(ids):
        erreurs.append(f"{identifiant} : chanson du catalogue introuvable.")

    images = set()
    for chanson in chansons:
        dossier = RACINE / "chansons" / chanson["folder"]
        if chanson["id"] != chanson["folder"]:
            erreurs.append(f"{chanson['folder']} : identifiant différent du dossier.")
        erreurs.extend(f"{chanson['folder']} : {e}" for e in erreurs_structure(chanson))
        sources = [page.get("image") for page in chanson.get("pages") or []] + [chanson.get("vignette")]
        for source in sources:
            if not source:
                continue
            image = (dossier / source).resolve()
            if not image.is_relative_to(dossier):
                erreurs.append(f"{chanson['id']} : image extérieure au dossier ({source}).")
            elif not image.is_file():
                erreurs.append(f"{chanson['id']} : image manquante ({source}).")
            else:
                images.add(image)

    # Images propres au recueil et au livret de partitions (js/chansons.js,
    # chargerRecueil et chargerPartitions).
    for livret in ("recueil", "partitions"):
        for nom in ("couverture.svg", "vignette.svg"):
            image = RACINE / "chansons" / livret / "images" / nom
            if image.is_file():
                images.add(image)
            else:
                erreurs.append(f"{livret} : image manquante ({nom}).")

    # Vérifier aussi les fichiers présents qui ne sont pas référencés.
    svgs = sorted((RACINE / "chansons").glob("*/images/*.svg"))
    for image in svgs:
        nom = image.relative_to(RACINE)
        try:
            svg = ET.parse(image).getroot()
            if svg.tag != "{http://www.w3.org/2000/svg}svg":
                raise ValueError("racine SVG ou espace de noms absent")
            cadre = [float(v) for v in svg.attrib.get("viewBox", "").split()]
            if len(cadre) != 4 or not all(math.isfinite(v) for v in cadre) or cadre[2] <= 0 or cadre[3] <= 0:
                raise ValueError("viewBox absent ou invalide")
            identifiers = [el.attrib["id"] for el in svg.iter() if "id" in el.attrib]
            if len(identifiers) != len(set(identifiers)):
                raise ValueError("identifiant SVG répété")
            refs = set()
            for el in svg.iter():
                for attr, value in el.attrib.items():
                    refs.update(re.findall(r"url\(#([^)]*)\)", value))
                    if attr in ("href", "{http://www.w3.org/1999/xlink}href") and value.startswith("#"):
                        refs.add(value[1:])
            if refs - set(identifiers):
                raise ValueError(f"référence SVG absente : {', '.join(sorted(refs - set(identifiers)))}")
        except (ET.ParseError, ValueError) as erreur:
            erreurs.append(f"{nom} : {erreur}.")

    erreurs.extend(erreurs_hors_ligne())

    for erreur in erreurs:
        print(erreur, file=sys.stderr)
    pages = sum(len(chanson.get("pages") or []) for chanson in chansons)
    print(f"{len(chansons)} chansons, {pages} pages, {len(images)} images référencées, {len(svgs)} SVG vérifiés.")
    hors_catalogue = sorted(set(ids) - set(catalogue))
    if hors_catalogue:
        print(f"Chansons hors catalogue : {', '.join(hors_catalogue)}.")
    print(f"{len(erreurs)} erreur(s).")
    return bool(erreurs)


if __name__ == "__main__":
    sys.exit(verifier())
