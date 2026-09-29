"""Meunier, tu dors — ton moulin va trop vite !"""
from base import *
from fantastique import personne
from chansons import *

ID = "meunier-tu-dors"


def campagne(S, graine=1, vent=False):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(nuage(160, 130, 0.8), nuage(640, 100, 0.6))
    collines(S, 600, "#b2f2bb", graine=graine)
    sol(S, 640, "#8ce99a", couleur2="#69db7c", y2=730)
    if vent:
        for k in range(4):
            S.add(chemin(f"M {40 + k * 20} {200 + k * 90} q 80 -30 160 0 t 160 0", stroke="#ffffff", sw=6, opacity=0.8))


def meunier_dort(x, y, s=1.0):
    return g([sac_farine(x - 60, y, 1.2 * s), meunier(x + 40, y, 1.2 * s, expr="dort", bras="croises"), zzz(x + 110, y - 330 * s, 1.2 * s)])


def farine(S, graine=1, nb=24):
    r = random.Random(graine)
    for _ in range(nb):
        S.add(cercle(r.uniform(0, 800), r.uniform(100, 600), r.uniform(4, 10), "#ffffff", opacity=0.9))


def couverture():
    S = Scene()
    campagne(S, 2)
    S.add(moulin_vent(520, 660, 1.1, rot=15, vitesse=True))
    S.add(meunier_dort(170, 780, 1.0))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"), rect(0, 230, 400, 40, "#8ce99a"))
    S.add(moulin_vent(200, 250, 0.45, rot=20))
    return S


def p01():
    S = Scene()
    campagne(S, 3)
    S.add(moulin_vent(560, 660, 1.0, rot=30, vitesse=True))
    S.add(meunier_dort(200, 790, 1.1))
    return S


def p02():
    S = Scene()
    campagne(S, 4, vent=True)
    S.add(moulin_vent(560, 660, 1.0, rot=60, vitesse=True))
    farine(S, 4)
    S.add(meunier_dort(200, 790, 1.1))
    return S


def p03():
    S = Scene()
    campagne(S, 5, vent=True)
    S.add(moulin_vent(620, 660, 0.9, rot=5, vitesse=True))
    S.add(perso("canard" if False else "cochon", 150, 790, 1.1, expr="furieux", bras="bouche"))
    S.add(perso("mouton", 330, 790, 1.0, expr="surpris", bras="haut"))
    S.add(perso("lapin", 480, 790, 0.95, expr="crie" if False else "furieux", bras="bouche"))
    S.add(texte(300, 330, "Meunier !", 64, "#c92a2a", contour="#fff", rot=-8))
    return S


def p04():
    S = Scene()
    campagne(S, 6)
    S.add(moulin_vent(560, 660, 1.0, rot=45))
    farine(S, 7, 10)
    S.add(meunier(240, 790, 1.5, expr="bouche_bee", bras="haut"))
    S.add(texte(250, 220, "Oh là là !", 60, "#1971c2", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-tu-dors.svg", p01), ("02-trop-fort.svg", p02), ("03-reveille-toi.svg", p03), ("04-oh-la-la.svg", p04),
]
