"""Sur le pont d'Avignon — on y danse tous en rond."""
from base import *
from fantastique import personne
from chansons import *

ID = "pont-avignon"


def decor(S):
    rhone(S, 520)
    S.add(pont_avignon(300, 470, 0.72))


def ronde(S, cx, cy, rx, ry, s=0.6, n_=6, graine=1):
    """Des danseurs qui se tiennent la main en rond ; on dessine d'abord ceux du fond."""
    r = random.Random(graine)
    danseurs = []
    for k in range(n_):
        a = 2 * math.pi * k / n_ + 0.3
        x, y = cx + math.cos(a) * rx, cy + math.sin(a) * ry
        danseurs.append((y, x, k))
    for y, x, k in sorted(danseurs):
        dame = k % 2 == 0
        habit = ["#f783ac", "#364fc7", "#fcc419", "#2f9e44", "#e64980", "#1098ad"][k % 6]
        peau = ["claire", "rosee", "doree", "brune", "foncee"][r.randrange(5)]
        S.add(danseur(x, y, s * (0.85 + (y - cy + ry) / (4 * ry)), dame=dame, habit=habit, peau=peau, expr="rire",
                      bras="large", chapeau_=False, cheveux=r.choice(["blond", "roux", "brun", "noir", "chatain"])))


def couverture():
    S = Scene()
    rhone(S, 560)
    S.add(pont_avignon(40, 470, 0.95))
    S.add(danseur(250, 460, 0.9, habit="#364fc7", expr="rire", bras="haut"))
    S.add(danseur(400, 460, 0.9, dame=True, habit="#f783ac", expr="rire", bras="haut"))
    S.add(envol_notes(470, 300, 740, 220, "#e8590c", 3, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#a5d8ff"), rect(0, 190, 400, 80, "#1c7ed6"))
    S.add(pont_avignon(-10, 180, 0.5))
    return S


def p01():
    S = Scene()
    rhone(S, 600)
    S.add(rect(0, 560, 800, 80, "#e9d8b4"), rect(0, 540, 800, 24, "#cbb58a"))
    ronde(S, 400, 610, 250, 60, 0.95)
    return S


def couplet(qui, bras, **k):
    S = Scene()
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(rect(0, 600, 800, 200, "#e9d8b4"), rect(0, 580, 800, 24, "#cbb58a"))
    for x in range(0, 800, 100):
        S.add(rect(x, 540, 60, 44, "#e9d8b4"))
    S.add(pont_avignon(560, 460, 0.35))
    return S


def p02():
    S = couplet("messieurs", "salut")
    S.add(danseur(250, 780, 1.4, habit="#364fc7", expr="fier", bras="salut"))
    S.add(danseur(560, 780, 1.4, habit="#c92a2a", peau="brune", cheveux="noir", expr="fier", bras="salut", flip=True))
    return S


def p03():
    S = couplet("dames", "large")
    S.add(danseur(250, 780, 1.4, dame=True, habit="#f783ac", expr="timide", bras="large"))
    S.add(danseur(560, 780, 1.4, dame=True, habit="#9775fa", peau="doree", cheveux="noir", expr="content", bras="large", flip=True))
    return S


def p04():
    S = couplet("musiciens", "donne")
    S.add(danseur(230, 780, 1.4, habit="#2f9e44", expr="souffle", bras="donne", chapeau_=False, objet=trompette(60, -96, 0.8)))
    S.add(danseur(560, 780, 1.4, habit="#fab005", peau="foncee", cheveux="noir", expr="rire", bras="porte", chapeau_=False))
    S.add(tambour_objet(560, 640, 1.0))
    S.add(envol_notes(300, 400, 520, 250, "#e8590c", 3, 0.9))
    return S


def p05():
    S = couplet("soldats", "salut")
    for x, c in [(200, "#1864ab"), (400, "#1864ab"), (600, "#1864ab")]:
        S.add(danseur(x, 780, 1.2, habit=c, jambes="#c92a2a", expr="fier", bras="salut", chapeau_=False, acc=()))
        S.add(place([rect(-44, -290, 88, 96, "#212529", rx=10), rect(-44, -212, 88, 14, OR), cercle(0, -260, 10, "#fa5252")], x, 780, 1.2))
    return S


def p06():
    S = Scene()
    rhone(S, 600)
    S.add(rect(0, 560, 800, 80, "#e9d8b4"), rect(0, 540, 800, 24, "#cbb58a"))
    ronde(S, 400, 610, 260, 60, 0.95, n_=7, graine=4)
    S.add(soleil(680, 110, 60, visage=True))
    S.add(texte(400, 150, "Tous en rond !", 60, "#e8590c", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-on-y-danse.svg", p01), ("02-les-messieurs.svg", p02), ("03-les-dames.svg", p03),
    ("04-les-musiciens.svg", p04), ("05-les-soldats.svg", p05), ("06-tous-en-rond.svg", p06),
]
