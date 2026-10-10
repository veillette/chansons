"""Compère Guilleri — parti à la chasse aux perdrix, carabi !"""
from base import *
from objets import pansement
from fantastique import personne
from chansons import *

ID = "compere-guilleri"
GUILLERI = dict(peau="rosee", cheveux="chatain", coiffure="courts", habit="#5c940d", robe=False, jambes="#8d5524")
DAMES = [dict(peau="doree", cheveux="brun", coiffure="chignon", habit="#f8f9fa", robe=True, acc=("noeud",), couleur_acc="#fa5252"),
         dict(peau="claire", cheveux="blond", coiffure="chignon", habit="#f8f9fa", robe=True, acc=("noeud",), couleur_acc="#fa5252")]


def guilleri(x, y, s=1.0, **k):
    return g([personne(x, y, s, **GUILLERI, **k),
              place([chemin("M -66 -190 Q -50 -250 0 -252 Q 50 -250 66 -190 Q 0 -206 -66 -190 Z", "#a0693a"),
                     chemin("M 30 -236 Q 60 -280 90 -270", stroke="#fa5252", sw=6)], x, y, s, flip=k.get("flip", False))])


def perdrix(x, y, s=1.0, **k):
    return oiseau(x, y, s, couleur="#a0693a", ventre="#e9d8c4", **k)


def campagne(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(150, 110, 0.7), nuage(640, 80, 0.8))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#c0eb75", couleur2="#a9e34b", y2=720)


def couverture():
    S = Scene()
    campagne(S, 2)
    S.add(arbre(560, 640, 1.6, "#51cf66", "#40c057"))
    S.add(guilleri(560, 380, 0.75, expr="rire", bras="salut"))
    S.add(perso("chien", 200, 790, 1.0, expr="joie", bras="haut"))
    S.add(perdrix(380, 300, 0.8, ailes="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff9db"), rect(0, 220, 400, 50, "#c0eb75"))
    S.add(perdrix(140, 230, 0.6), perdrix(260, 230, 0.6, flip=True))
    return S


def p01():
    S = Scene()
    campagne(S, 3)
    S.add(guilleri(400, 790, 1.5, expr="fier", bras="hanches"))
    S.add(texte(400, 180, "Carabi !", 70, "#5c940d", contour="#fff"))
    return S


def p02():
    S = Scene()
    campagne(S, 4)
    for k, (x, yy) in enumerate([(520, 720), (640, 760), (720, 690)]):
        S.add(perdrix(x, yy, 0.8, flip=True, expr="surpris" if k == 1 else "sourire"))
    S.add(guilleri(250, 790, 1.35, expr="malin", bras="montre", regard=(1, 0)))
    return S


def p03():
    S = Scene()
    campagne(S, 5)
    S.add(arbre(400, 640, 1.8, "#51cf66", "#40c057"))
    S.add(guilleri(440, 330, 0.8, expr="content", bras="salut"))
    S.add(perso("chien", 170, 790, 0.9, expr="joie", bras="haut"), perso("chien", 650, 790, 0.8, expr="rire", couleur="#a0693a"))
    S.add(mouvement(90, 700, 1.0), mouvement(760, 700, 1.0, rot=180))
    return S


def p04():
    S = Scene()
    campagne(S, 6)
    S.add(arbre(300, 640, 1.8, "#51cf66", "#40c057"))
    S.add(trait(430, 330, 560, 420, "#8d5524", 14))
    S.add(guilleri(560, 690, 0.9, expr="oups", bras="haut", rot=25))
    S.add(texte(600, 240, "Crac !", 70, "#e8590c", contour="#fff", rot=10))
    return S


def p05():
    S = Scene()
    interieur(S, "#e7f5ff", "#d0bfff", 560)
    S.add(lit(400, 640, 420, "#f8f9fa", "#a5d8ff"))
    S.add(guilleri(400, 800, 1.3, expr="content", bras="salut"))
    S.add(pansement(380, 610, 1.2, rot=-20))
    S.add(personne(120, 790, 1.0, expr="sourire", bras="bas", **DAMES[0]), personne(690, 790, 1.0, expr="rire", bras="bas", **DAMES[1]))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-un-petit-homme.svg", p01), ("02-les-perdrix.svg", p02), ("03-sur-un-arbre.svg", p03),
    ("04-la-branche.svg", p04), ("05-gueri.svg", p05),
]
