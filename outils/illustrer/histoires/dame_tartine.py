"""Il était une dame Tartine, dans un beau palais de beurre frais."""
from base import *
from contes import pain
from objets import gateau
from fantastique import personne, chateau
from chansons import *

ID = "dame-tartine"
TARTINE = dict(peau="rosee", cheveux="blond", coiffure="chignon", habit="#ffd43b", robe=True, acc=("noeud",), couleur_acc="#e8590c")
PRALINE = "#c87f4a"


def dame(x, y, s=1.0, **k):
    return personne(x, y, s, **TARTINE, **k)


def palais_beurre(x, y, s=1.0):
    return chateau(x, y, s, mur="#fff3bf", mur2="#ffec99", toit=PRALINE, drapeau="#e8590c", fenetres="#ffd8a8")


def dehors(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(150, 110, 0.7), nuage(640, 80, 0.8))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=720)


def salle_praline(S):
    S.add(rect(0, 0, 800, 560, PRALINE))
    r = random.Random(4)
    for _ in range(90):
        S.add(cercle(r.uniform(0, 800), r.uniform(0, 540), r.uniform(4, 9), r.choice(["#f1dcc3", "#8d5524", "#ffe8cc"])))
    S.add(rect(0, 560, 800, 240, "#f1c27d"))
    for k in range(9):
        for j in range(3):
            S.add(rect(k * 90 + (j % 2) * 45 - 10, 580 + j * 70, 80, 56, "#e0a458", rx=10, stroke="#c68642", stroke_width=3))
            S.add(cercle(k * 90 + (j % 2) * 45 + 30, 608 + j * 70, 4, "#c68642"))


def couverture():
    S = Scene()
    dehors(S, 2)
    S.add(palais_beurre(400, 640, 0.8))
    S.add(dame(400, 790, 1.2, expr="rire", bras="tient", objet=pain(68, -146, 0.6, rot=-20)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff9db"))
    S.add(pain(200, 150, 1.0, rot=-8))
    return S


def p01():
    S = Scene()
    dehors(S, 3)
    S.add(dame(400, 790, 1.6, expr="content", bras="tient", objet=pain(68, -146, 0.6, rot=-20)))
    return S


def p02():
    S = Scene()
    dehors(S, 4)
    S.add(palais_beurre(400, 700, 1.1))
    S.add(paillettes(150, 300, 1.0), paillettes(660, 260, 1.0))
    return S


def p03():
    S = Scene()
    salle_praline(S)
    S.add(dame(400, 790, 1.4, expr="miam", bras="ouverts"))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff9db", "#f1c27d", 560, papier="#fff3bf")
    S.add(fenetre(300, 120, 200, 170, rideaux="#ffffff"))
    for k in range(8):
        S.add(etoile5(300 + (k % 4) * 60 + 20, 140 + (k // 4) * 120, 8, "#868e96"))
    S.add(lit(400, 760, 460, "#ffe8cc", "#fff9db", bois="#e0a458"))
    for k in range(6):
        S.add(rect(190 + k * 70, 580, 56, 40, "#e0a458", rx=8, stroke="#c68642", stroke_width=3))
    S.add(gateau(660, 540, 0.5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-dame-tartine.svg", p01), ("02-palais-de-beurre.svg", p02), ("03-praline.svg", p03), ("04-la-chambre.svg", p04),
]
