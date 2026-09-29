"""Il court, il court, le furet — le jeu de la ronde et de l'anneau."""
from base import *
from fantastique import personne
from contes import foret
from chansons import *

ID = "il-court-le-furet"
ENFANTS = [
    dict(peau="claire", cheveux="roux", coiffure="courts", habit="#fa5252", robe=False, jambes="#495057"),
    dict(peau="brune", cheveux="noir", coiffure="tresses", habit="#cc5de8", robe=True),
    dict(peau="doree", cheveux="brun", coiffure="queue", habit="#20c997", robe=True),
    dict(peau="rosee", cheveux="blond", coiffure="herisses", habit="#339af0", robe=False, jambes="#1864ab"),
]


def bois(S, graine=1):
    foret(S, y=600, graine=graine)


def ronde(S, y=790, s=1.0, expr="rire", bras="large", xs=(120, 305, 495, 680), regards=None):
    for k, (x, e) in enumerate(zip(xs, ENFANTS)):
        S.add(personne(x, y, s, expr=expr, bras=bras, regard=(regards[k], 0) if regards else (0, 0), **e))


def couverture():
    S = Scene()
    bois(S, 2)
    ronde(S, 740, 0.95, bras="large")
    S.add(furet(380, 790, 1.2))
    S.add(mouvement(160, 740, 1.2))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#ebfbee"), rect(0, 210, 400, 60, "#8ce99a"))
    S.add(furet(180, 240, 1.0))
    return S


def p01():
    S = Scene()
    bois(S, 3)
    S.add(furet(360, 730, 2.0))
    S.add(mouvement(110, 650, 1.6))
    return S


def p02():
    S = Scene()
    bois(S, 4)
    ronde(S, 790, 1.1, "chante", "large")
    S.add(el("path", d="M 100 640 Q 400 700 700 640", fill="none", stroke="#fcc419", stroke_width=6))
    S.add(cercle(400, 670, 16, "none", stroke="#f59f00", stroke_width=8))
    return S


def p03():
    S = Scene()
    bois(S, 5)
    S.add(buisson(400, 720, 2.0))
    S.add(furet(430, 700, 1.3, expr="malin"))
    S.add(personne(140, 790, 1.2, expr="surpris", bras="montre", regard=(1, 0), **ENFANTS[1]))
    S.add(texte(560, 260, "Par ici !", 64, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    bois(S, 6)
    S.add(furet(260, 760, 1.4, flip=True))
    S.add(mouvement(470, 690, 1.4, rot=180))
    S.add(personne(640, 790, 1.2, expr="rire", bras="montre", flip=True, regard=(-1, 0), **ENFANTS[3]))
    S.add(texte(300, 260, "Par là !", 64, "#1971c2", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-il-court.svg", p01), ("02-la-ronde.svg", p02), ("03-par-ici.svg", p03), ("04-par-la.svg", p04),
]
