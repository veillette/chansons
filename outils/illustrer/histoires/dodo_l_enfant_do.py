"""Dodo, l'enfant do — la poule blanche et le petit coco."""
from base import *
from fantastique import personne
from fables import oeuf
from chansons import *

ID = "dodo-l-enfant-do"
MAMAN = dict(peau="brune", cheveux="noir", coiffure="boucles", habit="#9775fa", robe=True)


def bebe_berceau():
    return berceau(0, 0, 1.0, couleur="#d0bfff", bebe=bebe_dort(-40, -178, 1.0, "#ffd8a8"))


def ferme_nuit(S, graine=1):
    nuit(S, "#1c2a52", "#5c7cfa")
    etoiles(S, 36, graine, (0, 0, 800, 460))
    S.add(lune(640, 130, 55, fond_ciel="#243a73", croissant=True))
    collines(S, 600, "#364fc7", graine=graine)
    sol(S, 620, "#2b8a3e", couleur2="#2f9e44", y2=720)


def couverture():
    S = Scene()
    chambre_nuit(S, mur="#5f3dc4", papier="#7048e8", plancher="#5c4a3a")
    S.add(place(bebe_berceau(), 430, 770, 1.3))
    S.add(poule_blanche(700, 780, 0.9, expr="sourire"))
    S.add(etoile5(150, 180, 18), etoile5(260, 120, 12), etoile5(90, 330, 10))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#5f3dc4"), etoile5(60, 60, 12), etoile5(340, 50, 10))
    S.add(place(bebe_berceau(), 200, 262, 0.62))
    return S


def p01():
    S = Scene()
    chambre_nuit(S, mur="#5f3dc4", papier="#7048e8", plancher="#5c4a3a")
    S.add(place(bebe_berceau(), 400, 770, 1.45))
    S.add(zzz(520, 330, 1.2, "#fff3bf"))
    return S


def p02():
    S = Scene()
    chambre_nuit(S, mur="#5f3dc4", papier="#7048e8", plancher="#5c4a3a")
    S.add(place(bebe_berceau(), 480, 770, 1.3, rot=4))
    S.add(personne(180, 780, 1.4, expr="chante", bras="donne", regard=(1, 0), **MAMAN))
    S.add(envol_notes(250, 420, 460, 280, "#fff3bf", 3, 0.8))
    return S


def p03():
    S = Scene()
    ferme_nuit(S, 2)
    S.add(grange(400, 700, 1.3))
    S.add(poule_blanche(400, 700, 1.4, expr="sourire"))
    return S


def p04():
    S = Scene()
    interieur(S, "#ffe8cc", "#c68642", 600, papier="#ffd8a8")
    S.add(rect(0, 560, 800, 60, "#f6c453"))
    for k in range(14):
        S.add(trait(k * 60, 600, k * 60 + 30, 540, "#e0a800", 4))
    S.add(ellipse(400, 720, 170, 50, "#f6c453"), ellipse(400, 700, 140, 40, "#fcc419"))
    S.add(poule_blanche(330, 720, 1.2, expr="content"))
    S.add(oeuf(530, 700, 1.3, brille=True))
    S.add(coeur(560, 540, 0.7))
    return S


def p05():
    S = Scene()
    ferme_nuit(S, 4)
    S.add(maison(400, 700, 1.6, mur="#ffe8cc", toit="#c92a2a", lumiere=True))
    S.add(zzz(560, 360, 1.3, "#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-dodo.svg", p01), ("02-maman-chante.svg", p02), ("03-la-grange.svg", p03),
    ("04-le-coco.svg", p04), ("05-bonne-nuit.svg", p05),
]
