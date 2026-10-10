"""Cadet Rousselle — trois maisons, trois habits, trois beaux chats."""
from base import *
from fantastique import echelle
from fantastique import personne
from chansons import *

ID = "cadet-rousselle"
CADET = dict(peau="rosee", cheveux="roux", coiffure="herisses", habit="#e8590c", robe=False, jambes="#1971c2",
             acc=("col",))


def cadet(x, y, s=1.0, **k):
    return personne(x, y, s, **CADET, **k)


def village(S, graine=1):
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(nuage(150, 110, 0.7), nuage(640, 80, 0.8))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)


def trois_maisons(S, y=600, s=0.75, toit=True):
    for k, (x, mur) in enumerate([(160, "#ffe8cc"), (400, "#fff3bf"), (640, "#e7f5ff")]):
        S.add(maison(x, y + (k % 2) * 10, s, mur=mur, toit="#e8590c") if toit else maison_sans_toit(x, y + (k % 2) * 10, s, mur=mur))


def couverture():
    S = Scene()
    village(S, 2)
    trois_maisons(S, 590, 0.7, toit=False)
    for k, (x, yy) in enumerate([(170, 260), (420, 200), (640, 280)]):
        S.add(hirondelle(x, yy, 0.6, flip=k % 2 == 1, rot=-8))
    S.add(cadet(400, 790, 1.5, expr="rire", bras="ouverts"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"), rect(0, 220, 400, 50, "#8ce99a"))
    for k, x in enumerate((80, 200, 320)):
        S.add(maison_sans_toit(x, 236, 0.4, mur=("#ffe8cc", "#fff3bf", "#d0ebff")[k]))
    S.add(hirondelle(200, 60, 0.45))
    return S


def p01():
    S = Scene()
    village(S, 3)
    for k, (x, mur) in enumerate([(170, "#ffe8cc"), (420, "#fff3bf"), (660, "#e7f5ff")]):
        S.add(maison_sans_toit(x, 640, 0.95, mur=mur))
        S.add(texte(x, 330, str(k + 1), 80, "#e8590c", contour="#fff"))
    S.add(cadet(300, 800, 1.1, expr="fier", bras="montre", regard=(1, 0)))
    return S


def p02():
    S = Scene()
    village(S, 4)
    S.add(maison_sans_toit(400, 640, 1.6))
    S.add(nid(400, 280, 1.2), nid(250, 400, 0.9, 2), nid(560, 400, 0.9, 2))
    for k, (x, yy) in enumerate([(130, 200), (660, 160), (520, 120)]):
        S.add(hirondelle(x, yy, 0.7, flip=k == 1))
    return S


def p03():
    S = Scene()
    village(S, 5)
    S.add(cadet(400, 790, 1.7, expr="rire", bras="haut"))
    S.add(texte(160, 260, "Ah !", 80, "#e8590c", contour="#fff", rot=-12),
          texte(400, 200, "Ah !", 80, "#e8590c", contour="#fff"),
          texte(640, 260, "Ah !", 80, "#e8590c", contour="#fff", rot=12))
    return S


def p04():
    S = Scene()
    village(S, 6)
    S.add(trait(60, 260, 740, 280, ENCRE, 4), trait(60, 260, 60, 620, "#8d5524", 12), trait(740, 280, 740, 620, "#8d5524", 12))
    S.add(vetement(200, 360, 1.1, "chemise", "#fcc419"), vetement(400, 366, 1.1, "chemise", "#fcc419"))
    S.add(vetement(600, 372, 1.1, "chemise", "#ced4da"))
    S.add(texte(600, 400, "papier", 30, "#868e96"))
    S.add(cadet(400, 800, 1.4, expr="content", bras="salut"))
    return S


def p05():
    S = Scene()
    interieur(S, "#fff4e6", "#e8c39e", 560)
    S.add(poly([(0, 0), (800, 0), (800, 160), (400, 40), (0, 160)], "#c68642"))
    S.add(echelle(620, 560, 0.9, h=420))
    for k, x in enumerate((180, 340)):
        S.add(perso("chat", x, 760, 0.9, expr="dort" if k == 0 else "content", couleur=("#868e96", "#ffa94d")[k]))
    S.add(perso("chat", 640, 260, 0.6, expr="surpris", couleur="#343a40", bras="haut"))
    S.add(perso("souris", 480, 760, 0.5, expr="rire", bras="salut"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-trois-maisons.svg", p01), ("02-les-hirondelles.svg", p02), ("03-bon-enfant.svg", p03),
    ("04-trois-habits.svg", p04), ("05-trois-chats.svg", p05),
]
