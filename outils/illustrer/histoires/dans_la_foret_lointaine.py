"""Dans la forêt lointaine — le coucou répond au hibou."""
from base import *
from contes import foret
from chansons import *

ID = "dans-la-foret-lointaine"
COUCOU = dict(couleur="#868e96", ventre="#f1f3f5")


def bois(S, graine=1, soir=False):
    if soir:
        foret(S, "#5f3dc4", "#b197fc", 600, graine, sombre=True)
    else:
        foret(S, y=600, graine=graine)


def couverture():
    S = Scene()
    bois(S, 2, soir=True)
    S.add(chene_branches(400, 700, 1.0))
    S.add(oiseau(560, 330, 1.0, expr="chante", bec_ouvert=True, flip=True, **COUCOU))
    S.add(chouette(260, 330, 1.1, expr="content"))
    S.add(lune(680, 110, 40))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e5dbff"))
    S.add(chouette(130, 230, 0.8), oiseau(280, 220, 0.8, expr="chante", bec_ouvert=True, flip=True, **COUCOU))
    return S


def p01():
    S = Scene()
    bois(S, 3)
    S.add(texte(560, 220, "Coucou !", 60, "#5c7cfa", contour="#fff", rot=-6))
    S.add(oiseau(300, 280, 0.7, flip=False, ailes="haut", pattes=False, **COUCOU))
    return S


def p02():
    S = Scene()
    bois(S, 4)
    S.add(chene_branches(360, 760, 1.15))
    S.add(oiseau(560, 345, 1.2, expr="chante", bec_ouvert=True, flip=True, **COUCOU))
    S.add(texte(620, 170, "Coucou !", 56, "#5c7cfa", contour="#fff", rot=6))
    return S


def p03():
    S = Scene()
    bois(S, 5, soir=True)
    S.add(lune(120, 110, 45))
    S.add(chene_branches(400, 760, 1.1))
    S.add(chouette(560, 380, 1.4, expr="content", ailes="haut" if False else "bas"))
    S.add(texte(560, 150, "Hou hou !", 56, "#fcc419", contour="#343a40"))
    return S


def p04():
    S = Scene()
    bois(S, 6, soir=True)
    S.add(chene_branches(400, 760, 1.1))
    S.add(oiseau(560, 350, 1.1, expr="chante", bec_ouvert=True, flip=True, **COUCOU))
    S.add(chouette(230, 350, 1.2, expr="rire"))
    S.add(bulle(610, 110, 200, 90, "Coucou !", 36, pointe=(580, 250)))
    S.add(bulle(180, 90, 200, 90, "Hibou !", 36, pointe=(220, 200)))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-la-foret.svg", p01), ("02-le-coucou.svg", p02), ("03-le-hibou.svg", p03), ("04-coucou-hibou.svg", p04),
]
