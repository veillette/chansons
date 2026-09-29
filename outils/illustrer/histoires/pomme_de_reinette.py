"""Pomme de reinette et pomme d'api — la comptine pour choisir qui sera « le loup »."""
from base import *
from fantastique import personne
from chansons import *

ID = "pomme-de-reinette"
ENFANTS = [
    dict(peau="claire", cheveux="blond", coiffure="queue", habit="#fa5252", robe=True),
    dict(peau="foncee", cheveux="noir", coiffure="courts", habit="#339af0", robe=False, jambes="#364fc7"),
    dict(peau="doree", cheveux="brun", coiffure="tresses", habit="#51cf66", robe=True),
]


def verger(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(400, 90, 0.7))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)


def enfants(S, y=790, s=1.1, bras="bas", expr="rire", xs=(170, 400, 630)):
    for x, e in zip(xs, ENFANTS):
        S.add(personne(x, y, s, expr=expr, bras=bras, **e))


def couverture():
    S = Scene()
    verger(S, 2)
    S.add(pommier(170, 620, 0.9), pommier(640, 620, 0.8, graine=5))
    S.add(tapis_jeu(400, 740, 300, 50))
    enfants(S, 790, 1.15, "poing")
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff9db"))
    S.add(pomme_arbre(140, 150, 2.0, "#fa5252", -10), pomme_arbre(270, 150, 2.0, "#ffd43b", 10))
    return S


def p01():
    S = Scene()
    verger(S, 3)
    S.add(pommier(400, 640, 1.1))
    S.add(pomme_arbre(200, 740, 1.4, "#fa5252"), pomme_arbre(600, 740, 1.4, "#ffd43b"))
    S.add(texte(200, 660, "reinette", 38, "#c92a2a", contour="#fff"), texte(600, 660, "api", 38, "#e67700", contour="#fff"))
    return S


def p02():
    S = Scene()
    verger(S, 4)
    S.add(tapis_jeu(400, 700, 340, 70, "#e03131", "#fcc419"))
    enfants(S, 790, 1.2, "poing")
    return S


def p03():
    S = Scene()
    verger(S, 5)
    S.add(tapis_jeu(400, 700, 340, 70, "#868e96", "#ced4da"))
    enfants(S, 790, 1.2, "poing", "content")
    return S


def p04():
    S = Scene()
    verger(S, 6)
    S.add(personne(200, 790, 1.3, expr="malin", bras="tient", regard=(1, 0), **ENFANTS[0],
                   objet=maillet(68, -146, 1.0, -30)))
    S.add(personne(520, 790, 1.3, expr="rire", bras="hanches", **ENFANTS[1]))
    S.add(texte(560, 260, "Cache ton poing !", 50, "#1971c2", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-les-pommes.svg", p01), ("02-tapis-rouge.svg", p02), ("03-tapis-gris.svg", p03), ("04-cache-ton-poing.svg", p04),
]
