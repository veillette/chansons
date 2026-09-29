"""Fais dodo, Colas mon p'tit frère."""
from base import *
from objets import gateau, four, tasse, bol
from fantastique import personne
from chansons import *

ID = "fais-dodo"
SOEUR = dict(peau="rosee", cheveux="chatain", coiffure="tresses", habit="#f783ac", robe=True)
MAMAN = dict(peau="rosee", cheveux="chatain", coiffure="chignon", habit="#20c997", robe=True)
PAPA = dict(peau="rosee", cheveux="brun", coiffure="courts", habit="#4dabf7", robe=False, jambes="#495057", barbe="#4a2c17")


def colas(expr="dort"):
    return berceau(0, 0, 1.0, bebe=bebe_dort(-40, -178, 1.0, "#a5d8ff"))


def couverture():
    S = Scene()
    chambre_nuit(S)
    S.add(place(colas(), 470, 770, 1.3))
    S.add(personne(170, 780, 1.3, expr="chante", bras="donne", regard=(1, 0), **SOEUR))
    S.add(envol_notes(240, 420, 460, 300, "#fff3bf", 3, 0.9))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#364fc7"), lune(330, 60, 30))
    S.add(place(colas(), 200, 262, 0.72))
    return S


def p01():
    S = Scene()
    chambre_nuit(S)
    S.add(place(colas(), 480, 770, 1.35))
    S.add(personne(170, 780, 1.4, expr="chante", bras="donne", regard=(1, 0), **SOEUR))
    S.add(zzz(560, 380, 1.1, "#fff3bf"))
    return S


def p02():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 600, papier="#ffe8cc")
    S.add(fenetre(80, 90, 170, 150, "#1c2a52", nuit_=True, rideaux="#ffa94d"))
    S.add(four(620, 770, 1.2))
    S.add(table(330, 770, 300, 150, nappe="#ffc9c9"))
    S.add(gateau(330, 610, 1.0, bougies=0))
    S.add(personne(500, 780, 1.35, expr="content", bras="porte", **MAMAN, acc=("toque",)))
    S.add(texte(400, 60, "En haut…", 50, "#e8590c"))
    return S


def p03():
    S = Scene()
    interieur(S, "#e3fafc", "#c68642", 600, papier="#c5f6fa")
    S.add(fenetre(560, 90, 170, 150, "#1c2a52", nuit_=True, rideaux="#74c0fc"))
    S.add(rect(80, 470, 330, 130, "#adb5bd", rx=6), rect(80, 450, 330, 26, "#868e96", rx=6))
    S.add(el("rect", x=150, y=380, width=120, height=80, fill="#8d5524", rx=10))
    S.add(ellipse(210, 382, 60, 12, "#5c3a1e"), chemin("M 200 380 q -10 -30 0 -60 q 10 -30 0 -60", stroke="#ced4da", sw=6, opacity=0.8))
    S.add(personne(350, 780, 1.4, expr="content", bras="donne", flip=True, regard=(-1, 0), **PAPA,
                   objet=tasse(84, -70, 1.4, "#fa5252")))
    S.add(texte(400, 60, "… et en bas !", 50, "#1971c2"))
    return S


def p04():
    S = Scene()
    chambre_nuit(S)
    S.add(place(colas(), 480, 770, 1.35))
    S.add(personne(170, 780, 1.4, expr="dort", bras="calin", **SOEUR))
    S.add(ours_peluche(250, 790, 0.9))
    S.add(zzz(260, 360, 1.1, "#fff3bf"), zzz(560, 380, 1.1, "#fff3bf"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-fais-dodo.svg", p01), ("02-maman.svg", p02), ("03-papa.svg", p03), ("04-endormis.svg", p04),
]
