"""Frère Jacques — le moine qui oublie de sonner les matines."""
from base import *
from fantastique import personne
from chansons import *

ID = "frere-jacques"
AUBE_HAUT, AUBE_BAS = "#ffc9c9", "#fff3bf"


def cellule(S, matin=False):
    """Petite chambre du monastère, murs de pierre."""
    interieur(S, "#e9d8b4", "#a0693a", 600, plinthe="#8d5524")
    for k in range(0, 8):
        for j in range(0, 6):
            S.add(rect(k * 100 + (j % 2) * 50, j * 100 + 10, 90, 88, "#dfc9a0", rx=10, opacity=0.5))
    dehors = AUBE_BAS if matin else "#1c2a52"
    S.add(chemin("M 560 300 L 560 150 Q 620 80 680 150 L 680 300 Z", dehors, stroke="#c9b28a", sw=12))
    if matin:
        S.add(soleil(620, 270, 30, "#ffa94d", rayons=False))


def jacques_au_lit(S, expr="dort", x=340):
    S.add(lit(x, 790, 540, couleur="#fff", couverture="#8d5524", bois="#8d5524"))
    S.add(rect(x - 250, 560, 150, 70, "#fff", rx=30))
    S.add(moine(x - 150, 760, 1.4, expr=expr))
    S.add(rect(x - 270, 630, 540, 110, "#a0693a", rx=24))
    S.add(chemin(f"M {x - 250} 660 Q {x} 690 {x + 250} 660", stroke="#8d5524", sw=6))


def couverture():
    S = Scene()
    ciel(S, AUBE_HAUT, AUBE_BAS)
    S.add(soleil(150, 200, 60, "#ffa94d"))
    collines(S, 640, "#b2f2bb", graine=2)
    sol(S, 680, "#8ce99a", couleur2="#69db7c", y2=740)
    S.add(clocher(560, 720, 0.9, battant=18, ondes=True))
    S.add(moine(250, 780, 1.4, expr="baille", bras="haut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, AUBE_BAS))
    S.add(cloche(300, 30, 0.9, battant=16, ondes=True))
    S.add(moine(130, 262, 0.95, expr="baille", bras="haut"))
    return S


def p01():
    S = Scene()
    cellule(S)
    jacques_au_lit(S)
    S.add(zzz(320, 360, 1.6))
    return S


def p02():
    S = Scene()
    cellule(S, matin=True)
    jacques_au_lit(S, x=440)
    S.add(zzz(420, 360, 1.3))
    S.add(moine(120, 780, 1.2, expr="inquiet", bras="bouche", cheveux="gris", barbe="#e9ecef"))
    S.add(bulle(220, 190, 330, 90, "Dormez-vous ?", 38, pointe=(150, 420)))
    return S


def p03():
    S = Scene()
    ciel(S, AUBE_HAUT, AUBE_BAS)
    S.add(soleil(640, 460, 70, "#ffa94d"))
    collines(S, 640, "#b2f2bb", graine=3)
    sol(S, 680, "#8ce99a", couleur2="#69db7c", y2=740)
    S.add(clocher(300, 740, 1.0, battant=0))
    S.add(moine(620, 790, 1.1, expr="inquiet", bras="montre", flip=True, cheveux="gris", barbe="#e9ecef", regard=(-1, -1)))
    for x, y in [(520, 180), (600, 140), (680, 200)]:
        S.add(oiseau(x, y, 0.5, "#ff922b", ailes="haut", pattes=False))
    return S


def p04():
    S = Scene()
    S.add(rect(0, 0, 800, 800, "#fff3bf"))
    for k in range(12):
        a = math.radians(k * 30)
        S.add(poly([(400, 330), (400 + math.cos(a) * 700, 330 + math.sin(a) * 700), (400 + math.cos(a + 0.26) * 700, 330 + math.sin(a + 0.26) * 700)], "#ffe066"))
    S.add(cloche(400, 60, 1.9, battant=24, ondes=True))
    S.add(texte(150, 560, "Ding !", 70, "#e8590c", rot=-14), texte(400, 660, "Daing !", 70, "#e8590c"), texte(650, 560, "Dong !", 70, "#e8590c", rot=14))
    return S


def p05():
    S = Scene()
    cellule(S, matin=True)
    S.add(lit(440, 770, 480, couleur="#fff", couverture="#8d5524", bois="#8d5524"))
    S.add(moine(330, 770, 1.5, expr="surpris", bras="haut", larmes=False))
    S.add(mouvement(210, 360, 1.0, rot=-20), mouvement(520, 330, 1.0, rot=200))
    S.add(texte(620, 470, "Ding, daing, dong !", 34, "#e8590c", rot=8))
    return S


def p06():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    sol(S, 640, "#8ce99a", couleur2="#69db7c", y2=720)
    S.add(moine(140, 780, 1.1, expr="chante", bras="ouverts"))
    S.add(perso("ours", 320, 780, 1.0, expr="chante", bras="ouverts", habit="#fab005"))
    S.add(perso("lapin", 480, 780, 1.0, expr="chante", bras="haut", habit="#74c0fc"))
    S.add(perso("chat", 650, 780, 1.0, expr="chante", bras="ouverts", habit="#f783ac"))
    for k, (x, c) in enumerate([(140, "#e8590c"), (320, "#1971c2"), (480, "#2f9e44"), (650, "#ae3ec9")]):
        S.add(cercle(x, 480, 30, "#fff"), texte(x, 496, str(k + 1), 44, c))
        S.add(envol_notes(x - 30, 400 - k * 50, x + 40, 260 - k * 50, c, 2, 0.7, graine=k))
    S.add(texte(400, 110, "En canon !", 64, "#1971c2", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-il-dort.svg", p01), ("02-dormez-vous.svg", p02), ("03-le-clocher.svg", p03),
    ("04-ding-daing-dong.svg", p04), ("05-reveil.svg", p05), ("06-en-canon.svg", p06),
]
