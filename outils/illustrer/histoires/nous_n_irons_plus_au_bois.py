"""Nous n'irons plus au bois — les lauriers sont coupés : entrons dans la danse !"""
from base import *
from contes import panier
from fantastique import personne
from chansons import *

ID = "nous-n-irons-plus-au-bois"
ENFANTS = [
    dict(peau="rosee", cheveux="blond", coiffure="tresses", habit="#ff8787", robe=True),
    dict(peau="brune", cheveux="noir", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7"),
    dict(peau="doree", cheveux="roux", coiffure="queue", habit="#ffd43b", robe=True),
    dict(peau="claire", cheveux="chatain", coiffure="herisses", habit="#69db7c", robe=False, jambes="#2b8a3e"),
]
BELLE = dict(peau="rosee", cheveux="brun", coiffure="longs", habit="#cc5de8", robe=True, acc=("fleur",))


def bois(S, graine=1):
    ciel(S, "#a5d8ff", "#ebfbee")
    S.add(nuage(160, 100, 0.7), nuage(620, 80, 0.6))
    collines(S, 560, "#b2f2bb", graine=graine)
    for x in (60, 740):
        S.add(arbre(x, 600, 1.0, "#40c057", "#2f9e44"))
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)


def ronde(S, xs, y=790, s=1.0, bras="ouverts", expr="rire"):
    for k, x in enumerate(xs):
        S.add(personne(x, y + (k % 2) * 10, s, expr=expr, bras=bras, **ENFANTS[k % len(ENFANTS)]))


def couverture():
    S = Scene()
    bois(S, 2)
    for x in (230, 570):
        S.add(laurier(x, 620, 0.8, coupe=True))
    ronde(S, (130, 300, 500, 670), 790, 1.05)
    S.add(envol_notes(200, 300, 600, 220, "#2f9e44"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#ebfbee"), rect(0, 220, 400, 50, "#8ce99a"))
    S.add(laurier(120, 240, 0.5, coupe=True), laurier(280, 240, 0.5, coupe=True))
    S.add(coeur(200, 110, 0.9, "#ff6b6b"))
    return S


def p01():
    S = Scene()
    bois(S, 3)
    for k, x in enumerate((180, 400, 620)):
        S.add(laurier(x, 660 + (k % 2) * 20, 1.2, coupe=True))
    S.add(personne(400, 800, 1.1, expr="surpris", bras="joues", **ENFANTS[1]))
    return S


def p02():
    S = Scene()
    bois(S, 4)
    S.add(laurier(160, 650, 1.0, coupe=True))
    for k in range(5):
        S.add(ellipse(300 + k * 70, 700 + (k % 2) * 20, 30, 10, "#2f9e44", rot=k * 35))
    S.add(personne(470, 790, 1.4, expr="content", bras="porte", objet=panier(0, -70, 0.8, contenu="fleurs"), **BELLE))
    return S


def p03():
    S = Scene()
    bois(S, 5)
    ronde(S, (130, 300, 500, 670), 790, 1.05)
    S.add(texte(400, 200, "Entrez dans la danse !", 52, "#2f9e44", contour="#fff"))
    return S


def p04():
    S = Scene()
    bois(S, 6)
    for k, x in enumerate((160, 400, 640)):
        S.add(personne(x, 760 - (k % 2) * 60, 1.1, expr="rire", bras="haut", **ENFANTS[k]))
    for x, yy in [(280, 280), (520, 240), (400, 160)]:
        S.add(coeur(x, yy, 0.8, "#ff6b6b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-les-lauriers.svg", p01), ("02-la-belle.svg", p02), ("03-la-danse.svg", p03), ("04-sautez.svg", p04),
]
