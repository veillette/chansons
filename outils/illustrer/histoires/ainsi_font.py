"""Ainsi font, font, font les petites marionnettes."""
from base import *
from chansons import *

ID = "ainsi-font"
POUPEES = [
    dict(habit="#fa5252", cheveux="roux", coiffure="boucles"),
    dict(habit="#4dabf7", cheveux="blond", coiffure="courts", peau="claire"),
    dict(habit="#fcc419", cheveux="noir", coiffure="tresses", peau="brune"),
]


def couverture():
    S = Scene()
    theatre(S)
    S.add(marionnette(400, 610, 1.3, bras="haut", **POUPEES[0]))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff3bf"))
    S.add(marionnette(200, 262, 0.55, bras="haut", **POUPEES[1]))
    return S


def p01():
    S = Scene()
    theatre(S)
    for (x, rot), p in zip([(250, -6), (400, 0), (550, 6)], POUPEES):
        S.add(marionnette(x, 600, 0.95, bras="large", rot=rot, **p))
    return S


def p02():
    S = Scene()
    theatre(S)
    S.add(marionnette(300, 600, 1.1, bras="haut", rot=-14, **POUPEES[1]))
    S.add(chemin("M 190 560 A 120 40 0 1 0 420 560", stroke="#e8590c", sw=6))
    S.add(poly([(420, 560), (400, 540), (440, 540)], "#e8590c"))
    S.add(marionnette(560, 600, 0.9, bras="salut", rot=10, **POUPEES[2]))
    S.add(texte(400, 250, "1, 2, 3 !", 56, "#e8590c"))
    return S


def p03():
    S = Scene()
    theatre(S)
    for (x, y), p in zip([(250, 540), (400, 600), (550, 540)], POUPEES):
        S.add(marionnette(x, y, 0.95, bras="hanches", expr="rire", **p))
        S.add(mouvement(x - 10, y + 30, 0.8, rot=90))
    return S


def p04():
    S = Scene()
    theatre(S, rideau="#e64980")
    S.add(marionnette(400, 600, 1.2, bras="ouverts", expr="rire", **POUPEES[0]))
    S.add(coeur(200, 280, 0.8), coeur(600, 280, 0.8), etoile5(260, 200, 16, "#fcc419"), etoile5(540, 200, 16, "#fcc419"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-ainsi-font.svg", p01), ("02-trois-p-tits-tours.svg", p02), ("03-sautez.svg", p03), ("04-recommencez.svg", p04),
]
