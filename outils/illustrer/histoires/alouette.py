"""Alouette, gentille alouette — on lui chatouille la tête, le bec, les yeux…"""
from base import *
from fantastique import personne
from chansons import *

ID = "alouette"
BRUN, VENTRE = "#c49a6c", "#f6e7d3"
ENFANT = dict(peau="claire", cheveux="roux", coiffure="courts", habit="#4dabf7", robe=False, jambes="#364fc7")

# Parties du corps de l'oiseau (coordonnées locales d'oiseau(), avant l'échelle).
PARTIES = {
    "tete": (0, -104, 26), "bec": (0, -68, 16), "yeux": (0, -82, 30),
    "cou": (0, -38, 28), "ailes": (40, -60, 26), "pattes": (0, -12, 26),
}


def alouette(x, y, s=1.0, expr="rire", ailes="bas", flip=False, pattes=True, rot=0):
    """Alouette : petit oiseau brun avec une huppe."""
    huppe = place([poly([(-10, -108), (-4, -140), (4, -110)], _fonce()), poly([(0, -110), (10, -146), (12, -108)], _fonce())], 0, 0, 1)
    return g([place(huppe, x, y, s, flip=flip, rot=rot),
              oiseau(x, y, s, BRUN, VENTRE, expr=expr, ailes=ailes, flip=flip, pattes=pattes, rot=rot)])


def _fonce():
    return "#8f6a45"


def champ(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(soleil(660, 130, 55))
    collines(S, 560, "#d8f5a2", graine=graine)
    sol(S, 600, "#c0eb75", couleur2="#a9e34b", y2=700)
    r = random.Random(graine)
    for _ in range(18):
        S.add(fleur(r.uniform(20, 780), r.uniform(640, 790), r.uniform(0.4, 0.7), r.choice(["#ff6b6b", "#ffd43b", "#cc5de8"]), tige=30))


def chatouille(partie, expr="rire"):
    """Gros plan : la plume de l'enfant chatouille une partie de l'alouette."""
    S = Scene()
    champ(S, len(partie))
    x, y, s = 470, 720, 4.2
    px, py, r = PARTIES[partie]
    halo_x, halo_y = x + px * s, y + py * s
    S.add(cercle(halo_x, halo_y, r * s * 1.3, "#fff3bf", opacity=0.8))
    S.add(alouette(x, y, s, expr=expr, ailes="haut" if partie == "ailes" else "bas"))
    if partie == "ailes":
        S.add(cercle(x - px * s, halo_y, r * s * 1.3, "#fff3bf", opacity=0.5))
    S.add(plume(halo_x - 40, halo_y + 40, 1.6, rot=-60))
    for k in range(3):
        S.add(plume(120 + k * 90, 200 + (k % 2) * 60, 0.45, rot=40 + k * 50, couleur="#e9d8c4", bord="#c49a6c"))
    S.add(texte(130, 110, "Hi hi !", 56, "#e8590c", rot=-10))
    return S


def couverture():
    S = Scene()
    champ(S, 2)
    S.add(personne(230, 780, 1.4, expr="chante", bras="ouverts", **ENFANT))
    S.add(alouette(550, 700, 2.2, expr="chante", ailes="ouvertes"))
    S.add(envol_notes(560, 380, 760, 240, "#8f6a45", 3, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff9db"))
    S.add(alouette(200, 262, 1.5, expr="chante", ailes="ouvertes"))
    return S


def p01():
    S = Scene()
    champ(S, 3)
    S.add(personne(200, 780, 1.4, expr="chante", bras="ouverts", **ENFANT))
    S.add(alouette(560, 700, 2.4, expr="rire"))
    S.add(envol_notes(280, 420, 480, 300, "#e8590c", 3, 0.8))
    return S


def p08():
    S = Scene()
    champ(S, 9)
    S.add(personne(220, 780, 1.4, expr="rire", bras="salut", **ENFANT))
    S.add(alouette(560, 330, 2.0, expr="rire", ailes="ouvertes", pattes=False, rot=-10))
    S.add(envol_notes(420, 470, 700, 150, "#8f6a45", 4, 0.8))
    return S


IMAGES = [("couverture.svg", couverture), ("vignette.svg", vignette), ("01-alouette.svg", p01)]
for _k, _partie in enumerate(["tete", "bec", "yeux", "cou", "ailes", "pattes"], start=2):
    IMAGES.append((f"{_k:02d}-{_partie}.svg", (lambda p=_partie: chatouille(p))))
IMAGES.append(("08-envolee.svg", p08))
