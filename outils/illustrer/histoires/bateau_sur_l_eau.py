"""Bateau sur l'eau — et plouf, les enfants sont tombés dans l'eau !"""
from base import *
from fantastique import personne
from fables import riviere
from sciences import canard
from chansons import *

ID = "bateau-sur-l-eau"
ENFANTS = [
    dict(peau="claire", cheveux="blond", coiffure="courts", habit="#fa5252", robe=False, jambes="#364fc7"),
    dict(peau="foncee", cheveux="noir", coiffure="tresses", habit="#fcc419", robe=True),
]


def paysage(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(160, 110, 0.8), nuage(620, 80, 0.6), soleil(700, 120, 45))
    collines(S, 480, "#b2f2bb", graine=graine)
    sol(S, 480, "#8ce99a", couleur2="#69db7c", y2=540)
    S.add(rect(0, 540, 800, 260, "#4dabf7"))
    for k in range(5):
        yy = 590 + k * 45
        S.add(chemin(f"M {20 + k * 37} {yy} q 30 -12 60 0 t 60 0 M {420 + k * 23} {yy + 20} q 30 -12 60 0 t 60 0",
                     stroke="#a5d8ff", sw=5, opacity=0.8))


def passagers(expr="rire", bras="haut"):
    return [personne(-70, -40, 0.75, expr=expr, bras=bras, **ENFANTS[0]),
            personne(70, -40, 0.75, expr=expr, bras=bras, **ENFANTS[1])]


def couverture():
    S = Scene()
    paysage(S, 2)
    S.add(barque(400, 660, 1.3, passagers=passagers(), voile="#fff9db"))
    S.add(canard(130, 720, 0.7), canard(680, 740, 0.6, flip=True))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"), rect(0, 190, 400, 80, "#4dabf7"))
    S.add(barque(200, 210, 0.6, voile="#fff9db"))
    return S


def p01():
    S = Scene()
    paysage(S, 3)
    S.add(barque(400, 660, 1.4, passagers=passagers("chante", "large")))
    S.add(envol_notes(420, 320, 640, 200, "#1971c2", 3, 0.8))
    return S


def p02():
    S = Scene()
    paysage(S, 4)
    for x in (80, 260, 620):
        S.add(fleur(x, 520, 0.9, "#ff8787"))
    S.add(barque(470, 640, 1.2, passagers=passagers("content", "salut")))
    S.add(canard(150, 720, 0.8), canard(250, 760, 0.55))
    return S


def p03():
    S = Scene()
    paysage(S, 5)
    S.add(barque(400, 650, 1.3, passagers=passagers("surpris", "haut"), rot=-24))
    S.add(texte(400, 200, "Oh !", 80, "#e03131", contour="#fff"))
    return S


def p04():
    S = Scene()
    paysage(S, 6)
    S.add(barque(620, 720, 0.9, rot=170))
    S.add(personne(230, 820, 1.1, expr="rire", bras="haut", **ENFANTS[0]))
    S.add(personne(420, 835, 1.1, expr="rire", bras="haut", **ENFANTS[1]))
    S.add(rect(0, 720, 800, 80, "#4dabf7", opacity=0.92))
    S.add(eclaboussure(230, 800, 1.0, "#d0ebff"), eclaboussure(420, 815, 1.0, "#d0ebff"))
    S.add(texte(330, 250, "Plouf !", 90, "#1971c2", contour="#fff", rot=-6))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-bateau.svg", p01), ("02-au-bord-de-l-eau.svg", p02), ("03-chavire.svg", p03), ("04-plouf.svg", p04),
]
