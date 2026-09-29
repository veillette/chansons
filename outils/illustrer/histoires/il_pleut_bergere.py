"""Il pleut, il pleut, bergère — rentrer les moutons avant l'orage."""
from base import *
from objets import parapluie
from fantastique import personne
from fables import baton
from chansons import *

ID = "il-pleut-bergere"
BERGERE = dict(peau="rosee", cheveux="blond", coiffure="longs", habit="#f783ac", robe=True, acc=("fleur",))
BERGER = dict(peau="doree", cheveux="brun", coiffure="courts", habit="#40c057", robe=False, jambes="#5c3a1e")
MERE = dict(peau="doree", cheveux="brun", coiffure="chignon", habit="#9775fa", robe=True)
ANNE = dict(peau="doree", cheveux="brun", coiffure="queue", habit="#fcc419", robe=True)


def pluvieux(S, graine=1, sombre=False):
    if sombre:
        ciel(S, "#343a40", "#868e96")
    else:
        ciel(S, "#868e96", "#dee2e6")
    S.add(nuage(160, 110, 1.1, "#ced4da", ombre="#adb5bd"), nuage(560, 90, 1.3, "#ced4da", ombre="#adb5bd"))
    collines(S, 580, "#8ce99a" if not sombre else "#51cf66", graine=graine)
    sol(S, 600, "#69db7c", couleur2="#51cf66", y2=720)


def moutons(S, xs, y=770, s=0.9, flip=False, mouille=True):
    for k, x in enumerate(xs):
        S.add(mouton_pre(x, y + (k % 2) * 20, s, flip=flip, mouille=mouille))


def couverture():
    S = Scene()
    pluvieux(S, 2)
    S.add(chaumiere(620, 620, 0.7, lumiere=True))
    moutons(S, (420, 540), 760)
    S.add(personne(160, 790, 1.3, expr="content", bras="tient", regard=(1, 0), **BERGERE,
                   objet=parapluie(68, -146, 1.0, "#fa5252", "#e03131")))
    S.add(personne(300, 790, 1.2, expr="rire", bras="montre", regard=(1, 0), **BERGER))
    pluie(S, 70, 3)
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#dee2e6"), rect(0, 220, 400, 50, "#69db7c"))
    S.add(mouton_pre(140, 250, 0.7), mouton_pre(260, 262, 0.6))
    pluie(S, 30, 4, (0, 0, 400, 240))
    return S


def p01():
    S = Scene()
    pluvieux(S, 3)
    moutons(S, (380, 520, 660), 760)
    S.add(personne(170, 790, 1.35, expr="surpris", bras="haut", **BERGERE))
    S.add(baton(110, 800, 90, 560, "#a0693a", 10))
    pluie(S, 80, 5)
    return S


def p02():
    S = Scene()
    pluvieux(S, 4)
    S.add(chaumiere(640, 620, 0.75))
    moutons(S, (330, 450), 770, flip=False)
    S.add(personne(120, 790, 1.2, expr="rire", bras="course", regard=(1, 0), **BERGERE))
    S.add(personne(560, 790, 1.2, expr="joie", bras="salut", flip=True, regard=(-1, 0), **BERGER))
    pluie(S, 80, 6)
    return S


def p03():
    S = Scene()
    pluvieux(S, 5, sombre=True)
    for x in (80, 260, 700):
        S.add(arbre(x, 620, 1.1, "#2f9e44", "#2b8a3e"))
    S.add(eclair(440, 140, 1.3), eclair(620, 80, 0.8))
    moutons(S, (300, 520), 770)
    S.add(personne(420, 790, 1.2, expr="surpris", bras="joues", **BERGERE))
    pluie(S, 120, 7, couleur="#a5d8ff")
    return S


def p04():
    S = Scene()
    pluvieux(S, 6, sombre=True)
    S.add(texte(620, 200, "BOUM !", 70, "#fcc419", contour="#343a40", rot=8))
    moutons(S, (560, 680), 770)
    S.add(personne(230, 790, 1.3, expr="inquiet", bras="calin", **BERGERE))
    S.add(personne(380, 790, 1.35, expr="content", bras="tient", regard=(-1, 0), **BERGER,
                   objet=parapluie(-40, -250, 1.5, "#4dabf7", "#1c7ed6", rot=-20)))
    pluie(S, 110, 8, couleur="#a5d8ff")
    return S


def p05():
    S = Scene()
    pluvieux(S, 7)
    S.add(chaumiere(400, 660, 1.1, lumiere=True, porte_ouverte=True))
    S.add(personne(640, 790, 1.2, expr="content", bras="ouverts", flip=True, **MERE))
    S.add(personne(160, 790, 1.0, expr="rire", bras="salut", **ANNE))
    moutons(S, (300,), 790, 0.8)
    pluie(S, 50, 9)
    return S


def p06():
    S = Scene()
    interieur(S, "#ffe8cc", "#c68642", 600, papier="#ffd8a8")
    S.add(rect(40, 330, 260, 270, "#adb5bd", rx=8), rect(80, 420, 180, 180, "#343a40", rx=6))
    S.add(feu_bois(170, 590, 1.0))
    S.add(fenetre(560, 90, 170, 150, "#495057", rideaux="#e03131"))
    S.add(personne(380, 790, 1.2, expr="content", bras="calin", **BERGERE))
    S.add(personne(520, 790, 1.05, expr="rire", bras="donne", flip=True, **ANNE))
    S.add(personne(660, 790, 1.2, expr="sourire", bras="hanches", flip=True, **BERGER))
    S.add(mouton_pre(160, 790, 0.8, mouille=False), mouton_pre(260, 800, 0.7, mouille=False))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-il-pleut.svg", p01), ("02-ma-chaumiere.svg", p02), ("03-l-orage.svg", p03),
    ("04-le-tonnerre.svg", p04), ("05-la-cabane.svg", p05), ("06-bonsoir.svg", p06),
]
