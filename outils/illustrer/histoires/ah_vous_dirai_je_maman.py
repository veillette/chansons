"""Ah ! vous dirai-je, maman — les bonbons valent mieux que la raison."""
from base import *
from fantastique import personne
from chansons import *

ID = "ah-vous-dirai-je-maman"
ENFANT = dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#fcc419", robe=False, jambes="#1971c2")
MAMAN = dict(peau="brune", cheveux="noir", coiffure="chignon", habit="#e64980", robe=True)
PAPA = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#495057", robe=False, jambes="#343a40", acc=("lunettes",))


def salon(S, papier="#d3f9d8"):
    interieur(S, "#ebfbee", "#e8c39e", 600, papier=papier)
    S.add(fenetre(560, 90, 170, 150, "#a5d8ff", rideaux="#ffa94d"))
    S.add(cadre_mur(130, 150, 120, 100, "#ffd8a8"))


def couverture():
    S = Scene()
    salon(S)
    pluie_bonbons(S, 12, 3, (40, 60, 760, 460))
    S.add(personne(260, 790, 1.35, expr="content", bras="ouverts", **MAMAN))
    S.add(personne(520, 790, 1.1, expr="miam", bras="haut", **ENFANT))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff0f6"))
    for k, c in enumerate(("#ff6b6b", "#fcc419", "#51cf66", "#339af0", "#cc5de8")):
        S.add(bonbon(70 + k * 65, 120 + (k % 2) * 50, 1.2, c, -20 + k * 12))
    return S


def p01():
    S = Scene()
    salon(S)
    S.add(personne(250, 790, 1.4, expr="sourire", bras="hanches", regard=(1, 0), **MAMAN))
    S.add(personne(520, 790, 1.15, expr="inquiet", bras="bas", regard=(-1, 0), **ENFANT))
    S.add(bulle(560, 160, 220, 110, "Maman…", 40, pointe=(530, 470)))
    return S


def p02():
    S = Scene()
    salon(S, "#dbe4ff")
    S.add(etagere(80, 330, 220, objets=None), livres_pile(190, 330, 1.0))
    S.add(personne(260, 790, 1.45, expr="neutre", bras="montre", regard=(1, 0), **PAPA))
    S.add(personne(560, 790, 1.1, expr="baille", bras="bas", **ENFANT))
    S.add(texte(560, 320, "1 + 1 = 2", 44, "#364fc7", contour="#fff", rot=-6))
    return S


def p03():
    S = Scene()
    salon(S, "#ffdeeb")
    pluie_bonbons(S, 18, 5, (20, 40, 780, 520))
    S.add(personne(400, 790, 1.5, expr="miam", bras="haut", **ENFANT))
    S.add(bonbon(250, 730, 1.3, "#cc5de8", 20), bonbon(560, 740, 1.3, "#51cf66", -10))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-maman.svg", p01), ("02-papa.svg", p02), ("03-les-bonbons.svg", p03),
]
