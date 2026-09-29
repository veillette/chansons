"""Une poule sur un mur — qui picore du pain dur."""
from base import *
from fables import coq
from chansons import *

ID = "une-poule-sur-un-mur"


def cour(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(150, 110, 0.7), nuage(620, 90, 0.8), soleil(700, 110, 45))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#c3fae8", couleur2="#96f2d7", y2=720)
    S.add(mur_pierres(0, 520, 800, 170))


def poule(x, y, s=1.0, **k):
    k.setdefault("expr", "content")
    return coq(x, y, s, poule=True, **k)


def couverture():
    S = Scene()
    cour(S, 2)
    S.add(poule(400, 525, 2.0))
    S.add(pain_dur(560, 505, 1.2, -10))
    for x in (100, 700):
        S.add(fleur(x, 760, 1.0, "#ff6b6b"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"))
    S.add(mur_pierres(0, 190, 400, 80))
    S.add(poule(200, 194, 1.1))
    return S


def p01():
    S = Scene()
    cour(S, 3)
    S.add(poule(400, 525, 2.2, regard=(0, 0)))
    return S


def p02():
    S = Scene()
    cour(S, 4)
    S.add(pain_dur(470, 506, 1.5, 8), miettes_pain(470, 518, 1.0))
    S.add(poule(330, 525, 2.0, expr="miam", rot=18))
    return S


def p03():
    S = Scene()
    cour(S, 5)
    S.add(miettes_pain(400, 518, 1.4, graine=3, nb=5))
    for k, x in enumerate((160, 400, 640)):
        S.add(poule(x, 525, 1.5, expr="rire", rot=(-1) ** k * 16))
    S.add(texte(260, 300, "Picoti !", 60, "#e8590c", contour="#fff", rot=-8))
    S.add(texte(560, 250, "Picota !", 60, "#d6336c", contour="#fff", rot=8))
    return S


def p04():
    S = Scene()
    cour(S, 6)
    S.add(poule(560, 780, 1.8, expr="fier", flip=True, regard=(1, 0), rot=-6))
    S.add(mouvement(680, 700, 1.4, rot=0), miettes_pain(300, 518, 1.0, graine=5, nb=3))
    S.add(texte(220, 300, "Au revoir !", 56, "#1971c2", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-sur-un-mur.svg", p01), ("02-pain-dur.svg", p02), ("03-picoti.svg", p03), ("04-s-en-va.svg", p04),
]
