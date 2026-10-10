"""Jean Petit qui danse — du doigt, du pied, et de tout le reste !"""
from base import *
from fantastique import personne
from chansons import *

ID = "jean-petit-qui-danse"
JEAN = dict(peau="doree", cheveux="brun", coiffure="herisses", habit="#f08c00", robe=False, jambes="#1971c2", acc=("col",))
AMIS = [dict(peau="rosee", cheveux="blond", coiffure="queue", habit="#e64980", robe=True),
        dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#20c997", robe=True),
        dict(peau="claire", cheveux="roux", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7")]


def jean(x, y, s=1.0, **k):
    return personne(x, y, s, **JEAN, **k)


def scene_bal(S, graine=1):
    ciel(S, "#ffe8cc", "#fff9db")
    for k in range(9):
        x = 40 + k * 90
        S.add(cercle(x, 90 + (k % 2) * 30, 14, ("#fa5252", "#fcc419", "#4dabf7", "#69db7c")[k % 4]))
    S.add(chemin("M 0 80 Q 200 140 400 90 T 800 100", stroke="#868e96", sw=3))
    sol(S, 600, "#e8c39e", couleur2="#d9a066", y2=720, bosse=0)


def couverture():
    S = Scene()
    scene_bal(S)
    S.add(jean(400, 790, 1.6, expr="rire", bras="haut", rot=-6))
    S.add(envol_notes(150, 380, 330, 250, "#f08c00"), envol_notes(480, 250, 680, 380, "#f08c00"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff9db"))
    S.add(notes(140, 150, 1.2, "#f08c00"), croche(270, 170, 1.4, "#f08c00"))
    return S


def p01():
    S = Scene()
    scene_bal(S)
    S.add(jean(400, 790, 1.6, expr="chante", bras="ouverts", rot=6))
    S.add(mouvement(180, 560, 1.2), mouvement(620, 560, 1.2, rot=180))
    return S


def p02():
    S = Scene()
    scene_bal(S)
    S.add(jean(330, 790, 1.6, expr="content", bras="salut"))
    S.add(texte(560, 230, "le doigt !", 60, "#f08c00", contour="#fff"))
    S.add(eclat(445, 300, 0.7))
    return S


def p03():
    S = Scene()
    scene_bal(S)
    S.add(jean(400, 760, 1.5, expr="rire", bras="large", rot=-12))
    S.add(mouvement(300, 740, 1.0, rot=-20))
    S.add(texte(600, 230, "le pied !", 60, "#f08c00", contour="#fff"))
    return S


def p04():
    S = Scene()
    scene_bal(S)
    S.add(personne(140, 790, 1.0, expr="rire", bras="haut", **AMIS[0]), personne(660, 790, 1.0, expr="rire", bras="haut", **AMIS[1]))
    S.add(personne(530, 800, 1.0, expr="chante", bras="ouverts", **AMIS[2]))
    S.add(jean(300, 800, 1.2, expr="rire", bras="ouverts", rot=8))
    S.add(envol_notes(150, 300, 650, 240, "#f08c00", nb=5))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-jean-petit.svg", p01), ("02-le-doigt.svg", p02), ("03-le-pied.svg", p03), ("04-tous-ensemble.svg", p04),
]
