"""Malbrough s'en va-t-en guerre — et Madame l'attend du haut de sa tour."""
from base import *
from sciences import cheval
from fables import oeuf
from fantastique import personne, chevalier, tour_seule
from chansons import *

ID = "malbrough"
MADAME = dict(peau="rosee", cheveux="chatain", coiffure="chignon", habit="#e64980", robe=True, acc=("diademe",))


def madame(x, y, s=1.0, **k):
    return personne(x, y, s, **MADAME, **k)


def malbrough(x, y, s=1.0, **k):
    return chevalier(x, y, s, plumet="#c92a2a", habit="#ced4da", cape="#c92a2a", **k)


def campagne(S, graine=1, ciel_bas="#fff4e6"):
    ciel(S, "#a5d8ff", ciel_bas)
    S.add(nuage(150, 110, 0.7), nuage(640, 80, 0.8))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)


def couverture():
    S = Scene()
    campagne(S, 2)
    S.add(tour_seule(640, 620, 0.8, mur="#e9ecef", toit="#c92a2a"))
    S.add(madame(640, 380, 0.55, expr="triste", bras="salut"))
    S.add(cheval(380, 790, 1.6, "#a0693a"))
    S.add(malbrough(180, 800, 1.3, expr="fier", bras="salut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff4e6"), rect(0, 220, 400, 50, "#8ce99a"))
    S.add(tour_seule(200, 240, 0.4, mur="#e9ecef", toit="#c92a2a"))
    S.add(tambour_objet(320, 180, 0.5, "#c92a2a"))
    return S


def p01():
    S = Scene()
    campagne(S, 3)
    S.add(malbrough(300, 800, 1.5, expr="fier", bras="tient", objet=trompette(60, -150, 0.8, rot=-30)))
    S.add(tambour_objet(560, 620, 1.2, "#c92a2a"))
    S.add(envol_notes(400, 300, 700, 200, "#c92a2a"))
    return S


def p02():
    S = Scene()
    campagne(S, 4, "#fff0f6")
    for k, x in enumerate((90, 200, 310)):
        S.add(fleur(x, 740 + (k % 2) * 20, 1.2, ("#ff6b6b", "#ffd43b", "#cc5de8")[k]))
    for k, (x, c) in enumerate([(540, "#ffc9c9"), (620, "#a5d8ff"), (700, "#ffec99")]):
        S.add(oeuf(x, 760, 1.0, c, rot=(k - 1) * 12))
    S.add(madame(400, 790, 1.4, expr="content", bras="calin"))
    S.add(texte(400, 200, "Pâques ?", 64, "#c92a2a", contour="#fff"))
    return S


def p03():
    S = Scene()
    campagne(S, 5, "#ffe8cc")
    S.add(soleil(680, 130, 60))
    S.add(madame(400, 790, 1.5, expr="triste", bras="joues"))
    S.add(texte(400, 210, "Pas encore…", 60, "#c92a2a", contour="#fff"))
    return S


def p04():
    S = Scene()
    campagne(S, 6)
    S.add(tour_seule(330, 800, 1.2, mur="#e9ecef", toit="#c92a2a", h=520))
    S.add(madame(330, 300, 0.7, expr="inquiet", bras="salut"))
    S.add(cheval(660, 620, 0.5, "#a0693a"), malbrough(600, 625, 0.35, bras="salut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-s-en-va-t-en-guerre.svg", p01), ("02-a-paques.svg", p02), ("03-la-trinite.svg", p03), ("04-la-tour.svg", p04),
]
