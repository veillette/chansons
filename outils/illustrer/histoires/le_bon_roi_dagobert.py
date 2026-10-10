"""Le bon roi Dagobert — et sa culotte à l'envers."""
from base import *
from objets import tasse
from fantastique import roi, jardin_chateau, couronne_objet
from chansons import *

ID = "le-bon-roi-dagobert"
CULOTTE = "#4dabf7"
ELOI = dict(peau="doree", cheveux="gris", barbe="#e9ecef")


def dagobert(x, y, s=1.0, envers=True, **k):
    """Le roi en culotte bleue ; « à l'envers », elle est enfilée… sur sa tête !"""
    if not envers:
        return roi(x, y, s, jambes=CULOTTE, **k)
    return g([roi(x, y, s, jambes="#f1f3f5", **k), vetement(x, y - 250 * s, 0.85 * s, "culotte", CULOTTE, rot=180)])


def eloi(x, y, s=1.0, **k):
    return moine(x, y, s, **ELOI, **k)


def couverture():
    S = Scene()
    jardin_chateau(S, chateau_s=0.7)
    S.add(eloi(600, 790, 1.2, expr="surpris", bras="montre", flip=True, regard=(-1, 0)))
    S.add(dagobert(300, 800, 1.5, expr="oups", bras="ouverts"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#f3f0ff"))
    S.add(couronne_objet(200, 120, 1.0, brille=True))
    S.add(vetement(200, 210, 0.45, "culotte", CULOTTE, rot=180))
    return S


def p01():
    S = Scene()
    interieur(S, "#f3f0ff", "#d0bfff", 560, papier="#e5dbff")
    S.add(fenetre(560, 160, 170, 170, rideaux="#7048e8"))
    S.add(dagobert(330, 790, 1.6, expr="fier", bras="hanches"))
    S.add(texte(660, 470, "?", 110, "#7048e8", contour="#fff"))
    return S


def p02():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6, chateau_x=600)
    S.add(eloi(560, 790, 1.35, expr="surpris", bras="montre", flip=True, regard=(-1, 0)))
    S.add(dagobert(240, 800, 1.35, expr="oups", bras="joues"))
    return S


def p03():
    S = Scene()
    jardin_chateau(S, chateau_s=0.6, chateau_x=220)
    S.add(eloi(620, 790, 1.2, expr="content", bras="bas", flip=True, regard=(-1, 0)))
    S.add(dagobert(360, 800, 1.5, envers=False, expr="rire", bras="haut"))
    S.add(eclat(360, 560, 1.0))
    return S


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(160, 110, 0.7), nuage(620, 90, 0.6))
    collines(S, 560, "#b2f2bb", graine=6)
    sol(S, 600, "#c0eb75", couleur2="#a9e34b", y2=720)
    S.add(dagobert(260, 800, 1.3, envers=False, expr="surpris", bras="haut", rot=-6))
    S.add(mouvement(150, 640, 1.4))
    S.add(perso("lapin", 600, 800, 1.2, expr="malin", bras="haut", flip=True))
    S.add(mouvement(730, 640, 1.2, rot=180))
    return S


def p05():
    S = Scene()
    mer(S, 520, graine=2)
    S.add(barque(400, 640, 1.6, "#7048e8", passagers=[dagobert(0, -40, 0.75, envers=False, expr="miam", bras="tient",
                                                                       objet=tasse(68, -146, 1.4, "#fcc419"))]))
    S.add(vagues_devant(680))
    S.add(texte(400, 160, "Le roi boit !", 64, "#7048e8", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-a-l-envers.svg", p01), ("02-saint-eloi.svg", p02), ("03-a-l-endroit.svg", p03),
    ("04-le-lapin.svg", p04), ("05-sur-la-mer.svg", p05),
]
