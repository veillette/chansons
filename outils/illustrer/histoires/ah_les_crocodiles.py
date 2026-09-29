"""Ah ! les crocodiles — le crocodile qui partait combattre les éléphants."""
from base import *
from chansons import *

ID = "ah-les-crocodiles"
CHAPEAU = "#f8f9fa"


def petits(S, x, y, s=0.32, expr="triste", larmes=False):
    for k in range(3):
        S.add(crocodile(x + k * 150 * s / 0.32, y + (k % 2) * 22, s, expr=expr, larmes=larmes and k == 1, flip=True))


def poussiere(S, x, y, s=1.0):
    for dx, dy, r in [(0, 0, 40), (-50, 10, 30), (40, 14, 26), (-90, 20, 22), (-20, -26, 26)]:
        S.add(cercle(x + dx * s, y + dy * s, r * s, "#e9d8b4", opacity=0.8))


def couverture():
    S = Scene()
    nil(S, 600)
    S.add(palmier(700, 640, 0.9), palmier(90, 650, 0.7))
    S.add(crocodile(360, 760, 0.9, expr="fier", chapeau_=CHAPEAU, tambour=True, marche=0.6))
    S.add(envol_notes(520, 560, 740, 430, "#e8590c", 3, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff4e6"), rect(0, 220, 400, 50, "#f4d58d"))
    S.add(crocodile(170, 250, 0.52, expr="rire", chapeau_=CHAPEAU))
    return S


def p01():
    S = Scene()
    nil(S, 600)
    S.add(palmier(90, 650, 0.8))
    S.add(crocodile(330, 700, 1.0, expr="sourire", chapeau_=CHAPEAU))
    petits(S, 430, 790, 0.36, expr="triste", larmes=True)
    S.add(bulle(600, 300, 300, 90, "Au revoir !", 38, pointe=(560, 480)))
    return S


def p02():
    S = Scene()
    nil(S, 600)
    S.add(crocodile(440, 770, 1.05, expr="fier", chapeau_=CHAPEAU, marche=-0.8))
    poussiere(S, 150, 740, 1.3)
    poussiere(S, 60, 700, 0.9)
    S.add(perso("elephant", 720, 560, 0.5, expr="neutre", flip=True))
    return S


def refrain_scene(S, soir=False):
    if soir:
        nil(S, 560, "#ffa94d", "#ffe8cc")
    else:
        nil(S, 560)
    S.add(rect(0, 560, 800, 240, "#4dabf7"))
    for k in range(6):
        S.add(chemin(" ".join(f"M {(k % 2) * 60 + i * 130} {600 + k * 34} q 25 -12 50 0" for i in range(7)), stroke="#a5d8ff", sw=5))
    for x, y, s, e in [(200, 700, 0.6, "chante"), (470, 640, 0.5, "rire"), (560, 780, 0.65, "chante")]:
        S.add(crocodile(x, y, s, expr=e, chapeau_=CHAPEAU if x == 430 else None))
        S.add(rect(x - 170 * s / 0.45, y - 20, 360 * s / 0.45 + 60, 60, "#4dabf7"))
        S.add(chemin(f"M {x - 150 * s / 0.45} {y - 20} q 40 -14 80 0 q 40 14 80 0 q 40 -14 80 0 q 40 14 80 0", stroke="#a5d8ff", sw=5))


def p03():
    S = Scene()
    refrain_scene(S)
    S.add(texte(400, 360, "Ah ! les crocrocro…", 58, "#e8590c", contour="#fff"))
    return S


def p04():
    S = Scene()
    nil(S, 600)
    S.add(crocodile(330, 770, 1.1, expr="chante", chapeau_=CHAPEAU, tambour=True, marche=0.4))
    S.add(envol_notes(620, 520, 760, 280, "#e8590c", 4, 1.0, graine=2))
    S.add(texte(620, 200, "Une, deux !", 46, "#e8590c", rot=-8))
    return S


def p05():
    S = Scene()
    nil(S, 600)
    S.add(crocodile(260, 790, 1.2, expr="furieux", gueule=True, chapeau_=CHAPEAU))
    for x, y in [(640, 250), (720, 330)]:
        S.add(oiseau(x, y, 0.8, "#fcc419", "#fff9db", expr="surpris", ailes="haut", pattes=False, flip=True))
    return S


def p06():
    S = Scene()
    ciel(S, "#a9e34b", "#ebfbee")
    for x, h in [(80, 1.1), (300, 1.0), (560, 1.2), (760, 1.0)]:
        S.add(arbre(x, 620, h, feuillage="#37b24d", feuillage2="#2f9e44"))
    sol(S, 620, "#94d82d", couleur2="#82c91e", y2=720)
    S.add(crocodile(190, 780, 0.7, expr="fier", chapeau_=CHAPEAU))
    for x, esp, e in [(470, "lievre", "surpris"), (600, "lion", "oups"), (720, "chevre", "inquiet")]:
        S.add(perso(esp, x, 760, 0.8, expr=e, bras="haut", regard=(-1, 0)))
        S.add(mouvement(x + 90, 620, 0.9, rot=180))
    return S


def p07():
    S = Scene()
    nil(S, 600)
    S.add(perso("elephant", 590, 780, 1.6, expr="fache", bras="hanches", flip=True))
    S.add(crocodile(200, 770, 0.55, expr="surpris", chapeau_=CHAPEAU))
    return S


def p08():
    S = Scene()
    nil(S, 480)
    S.add(rect(0, 560, 800, 240, "#4dabf7"))
    for k in range(3):
        S.add(cercle(300 + (k - 1) * 70, 560 - k % 2 * 40, 26, "#a5d8ff"), goutte(260 + k * 50, 500 - k * 30, 0.9, "#74c0fc"))
    S.add(chemin("M 190 600 q 110 -60 220 0", stroke="#e7f5ff", sw=10))
    S.add(cercle(300, 610, 26, VERT_CROCO), oeil(304, 606, "grand", (1, 0), sclere=True))
    S.add(ellipse(300, 624, 120, 16, "#1c7ed6", opacity=0.4))
    S.add(place(chemin("M -70 0 Q -10 -94 50 0 Z", CHAPEAU) + cercle(-10, -34, 10, "#fa5252"), 470, 640, 0.8, rot=20))
    S.add(perso("elephant", 620, 560, 1.2, expr="rire", bras="hanches", flip=True))
    return S


def p09():
    S = Scene()
    nil(S, 600)
    S.add(crocodile(260, 700, 0.9, expr="content"))
    petits(S, 330, 790, 0.34, expr="rire")
    S.add(perso("elephant", 690, 600, 0.7, expr="chante", bras="haut", flip=True))
    S.add(envol_notes(600, 420, 760, 260, "#7950f2", 3, 0.7))
    S.add(coeur(400, 470, 0.9))
    return S


def p10():
    S = Scene()
    refrain_scene(S, soir=True)
    S.add(texte(400, 360, "N'en parlons plus !", 58, "#c92a2a", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-au-revoir.svg", p01), ("02-la-poussiere.svg", p02), ("03-refrain.svg", p03),
    ("04-marche-militaire.svg", p04), ("05-la-gueule.svg", p05), ("06-tout-tremblants.svg", p06),
    ("07-l-elephant.svg", p07), ("08-la-riviere.svg", p08), ("09-le-retour.svg", p09), ("10-refrain-fin.svg", p10),
]
