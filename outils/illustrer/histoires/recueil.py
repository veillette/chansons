"""Couverture et vignette du recueil qui regroupe toutes les chansons."""
from base import *
from fantastique import personne
from chansons import *

ID = "recueil"


def couverture():
    S = Scene()
    nuit(S, "#3b5bdb", "#9775fa")
    etoiles(S, 40, 7, (0, 0, 800, 520))
    S.add(lune(620, 170, 70, visage=True))
    collines(S, 640, "#7048e8", graine=4)
    sol(S, 660, "#8ce99a", couleur2="#69db7c", y2=740)
    S.add(personne(170, 780, 1.2, peau="brune", cheveux="noir", coiffure="tresses", habit="#fcc419", expr="chante", bras="ouverts"))
    S.add(crocodile(420, 770, 0.55, expr="rire", gueule=False))
    S.add(souris_verte(600, 780, 1.0, expr="chante", bras="haut"))
    S.add(personne(720, 780, 0.9, peau="claire", cheveux="blond", coiffure="courts", habit="#4dabf7", robe=False, expr="rire", bras="salut", flip=True))
    S.add(envol_notes(120, 560, 700, 380, "#fff3bf", 6, 1.0, graine=3))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e5dbff", rx=0))
    S.add(croche(120, 170, 2.6, "#5f3dc4", rot=-8), notes(200, 150, 1.6, "#7950f2"))
    S.add(etoile5(330, 60, 22, "#fcc419"), etoile5(60, 70, 14, "#fcc419"))
    return S


IMAGES = [("couverture.svg", couverture), ("vignette.svg", vignette)]
