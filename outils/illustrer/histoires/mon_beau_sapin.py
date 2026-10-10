"""Mon beau sapin, roi des forêts, que j'aime ta verdure !"""
from base import *
from fantastique import personne
from chansons import *

ID = "mon-beau-sapin"
ENFANTS = [dict(peau="rosee", cheveux="blond", coiffure="queue", habit="#fa5252", robe=True),
           dict(peau="brune", cheveux="noir", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7")]


def hiver(S, nuit_=False, graine=1):
    if nuit_:
        nuit(S)
        etoiles(S, 40, graine)
    else:
        ciel(S, "#a5d8ff", "#e7f5ff")
    collines(S, 560, "#e7f5ff", graine=graine)
    sol(S, 600, "#f8f9fa", couleur2="#e9ecef", y2=720)


def couverture():
    S = Scene()
    hiver(S, graine=2)
    for x in (90, 710):
        S.add(sapin(x, 620, 0.9, neige=True))
    S.add(sapin(400, 760, 2.1, neige=True))
    S.add(etoile5(400, 160, 34, OR))
    flocons(S, 40, 3)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"), rect(0, 230, 400, 40, "#f8f9fa"))
    S.add(sapin(200, 250, 0.7, neige=True))
    return S


def p01():
    S = Scene()
    hiver(S, graine=3)
    for k, x in enumerate((80, 200, 600, 720)):
        S.add(sapin(x, 620 + (k % 2) * 20, 0.8))
    S.add(sapin(400, 700, 1.8))
    S.add(personne(250, 800, 0.9, expr="rire", bras="ouverts", **ENFANTS[0]), personne(560, 800, 0.9, expr="content", bras="salut", **ENFANTS[1]))
    return S


def p02():
    S = Scene()
    hiver(S, graine=4)
    for k, x in enumerate((120, 280, 560, 700)):
        S.add(arbre_nu(x, 640 + (k % 2) * 20, 0.9, neige=True))
    S.add(sapin(420, 740, 1.6, neige=True))
    flocons(S, 50, 5)
    return S


def p03():
    S = Scene()
    hiver(S, graine=5)
    S.add(soleil(660, 130, 55))
    S.add(sapin(400, 760, 2.0, neige=True))
    S.add(eclat(400, 300, 1.4, "#fff3bf"))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 560, papier="#ffe8cc")
    S.add(fenetre(560, 120, 170, 160, dehors="#364fc7", nuit_=True, rideaux="#c92a2a"))
    S.add(sapin_decore(330, 700, 1.5))
    S.add(jouet_cheval(620, 760, 0.8))
    return S


def p05():
    S = Scene()
    hiver(S, nuit_=True, graine=6)
    S.add(sapin(400, 760, 2.0, neige=True))
    S.add(etoile5(400, 120, 36, OR), eclat(400, 120, 1.0, OR))
    flocons(S, 40, 7)
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-roi-des-forets.svg", p01), ("02-l-hiver.svg", p02), ("03-ta-parure.svg", p03),
    ("04-noel.svg", p04), ("05-tes-verts-sommets.svg", p05),
]
