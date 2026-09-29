"""Promenons-nous dans les bois — pendant que le loup s'habille."""
from base import *
from fantastique import personne
from chansons import *

ID = "promenons-nous"
ENFANTS = [
    dict(peau="claire", cheveux="blond", coiffure="queue", habit="#fa5252", robe=True),
    dict(peau="brune", cheveux="noir", coiffure="courts", habit="#fab005", robe=False, jambes="#1971c2"),
    dict(peau="doree", cheveux="brun", coiffure="tresses", habit="#4dabf7", robe=True),
]
CHEMISE, CULOTTE, CHAUSSETTES, BOTTES = "#4dabf7", "#e03131", "#fcc419", "#5c3a1e"


def bois(S, graine=1):
    ciel(S, "#b2f2bb", "#ebfbee")
    for x, s in [(-40, 1.1), (180, 0.8), (420, 0.9), (650, 1.0), (860, 1.1)]:
        S.add(sapin(x, 600, s * 1.4, "#2b8a3e", "#2f9e44"))
    sol(S, 600, "#69db7c", couleur2="#51cf66", y2=700)
    S.add(chemin("M 300 800 Q 380 700 420 600 L 460 600 Q 470 700 520 800 Z", "#e9d8b4"))
    r = random.Random(graine)
    for _ in range(10):
        S.add(champignon(r.uniform(30, 770), r.uniform(640, 790), r.uniform(0.4, 0.7)))


def enfants(S, y=780, s=1.1, expr="rire", bras="bas", xs=(170, 400, 630), flip=False):
    for x, e in zip(xs, ENFANTS):
        S.add(personne(x, y, s, expr=expr, bras=bras, flip=flip, **e))


def cabane(S):
    interieur(S, "#e9d8b4", "#8d5524", 600, papier="#dfc9a0", plinthe="#5c3a1e")
    for k in range(8):
        S.add(trait(0, 60 + k * 70, 800, 60 + k * 70, "#c9a47e", 4))
    S.add(fenetre(580, 110, 160, 150, "#b2f2bb", cadre="#8d5524"))
    S.add(tapis(400, 720, 250, 50, "#ff8787", "#e03131"))


def loup(x, y, s=1.4, etape=0, expr="malin", bras="bas", objet=None):
    """Le loup à différentes étapes de l'habillage :
    0 rien, 1 culotte, 2 + chemise, 3 + chaussettes, 4 + bottes, 5 + chapeau et lunettes."""
    habit = CHEMISE if etape >= 2 else None
    acc = ("chapeau", "lunettes") if etape >= 5 else ()
    m = [perso("loup", x, y, s, expr=expr, bras=bras, habit=habit, acc=acc, couleur_acc="#343a40", objet=objet)]
    if etape >= 1:
        m.append(place([rect(-50, -58, 100, 30, CULOTTE, rx=8), rect(-50, -36, 46, 26, CULOTTE, rx=6), rect(4, -36, 46, 26, CULOTTE, rx=6), rect(-50, -60, 100, 10, "#c92a2a", rx=4)], x, y, s))
    if etape >= 3:
        m.append(place([rect(-38, -22, 28, 22, CHAUSSETTES, rx=6), rect(10, -22, 28, 22, CHAUSSETTES, rx=6)], x, y, s))
    if etape >= 4:
        m.append(place([rect(-46, -24, 38, 28, BOTTES, rx=8), rect(8, -24, 38, 28, BOTTES, rx=8)], x, y, s))
    return g(m)


def couverture():
    S = Scene()
    bois(S, 2)
    S.add(buisson_cache(650, 640, 1.2, yeux_=True))
    enfants(S, 790, 1.15, "rire", "large", xs=(150, 330, 500))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#ebfbee"), sapin(60, 240, 0.8, "#2b8a3e"), sapin(340, 240, 0.8, "#2b8a3e"))
    S.add(perso("loup", 200, 262, 0.95, expr="malin", bras="salut", acc=("chapeau",), couleur_acc="#343a40"))
    return S


def p01():
    S = Scene()
    bois(S, 3)
    enfants(S, 790, 1.2, "rire", "large")
    return S


def p02():
    S = Scene()
    bois(S, 4)
    S.add(arbre_loup(640, 700, 1.0))
    S.add(chemin("M 700 640 Q 760 600 740 540 Q 780 600 720 660 Z", "#868e96"))
    enfants(S, 790, 1.1, "malin", "bouche", xs=(140, 300, 460))
    return S


def habillage(etape, dit, objet=None, bras="bas"):
    S = Scene()
    cabane(S)
    S.add(loup(380, 760, 1.8, etape, expr="concentre" if etape < 5 else "malin", bras=bras, objet=objet))
    S.add(bulle(500, 90, 520, 100, dit, 40, pointe=(470, 330)))
    return S


def p03():
    return habillage(0, "Je mets ma culotte !", bras="porte", objet=vetement(0, -80, 0.8, "culotte", CULOTTE))


def p04():
    return habillage(1, "Je mets ma chemise !", bras="porte", objet=vetement(0, -90, 0.75, "chemise", CHEMISE))


def p05():
    return habillage(2, "Je mets mes chaussettes !", bras="porte", objet=vetement(0, -80, 0.7, "chaussettes", CHAUSSETTES))


def p06():
    return habillage(3, "Je mets mes bottes !", bras="porte", objet=vetement(0, -80, 0.6, "bottes", BOTTES))


def p07():
    return habillage(5, "Et mes lunettes !", bras="salut")


def p08():
    S = Scene()
    bois(S, 8)
    S.add(loup(620, 780, 1.4, 5, expr="rire", bras="haut"))
    S.add(mouvement(760, 560, 1.3, rot=180))
    enfants(S, 790, 1.0, "rire", "haut", xs=(90, 240, 390))
    S.add(texte(400, 120, "J'arrive !", 72, "#e03131", contour="#fff", rot=-6))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-dans-les-bois.svg", p01), ("02-si-le-loup.svg", p02), ("03-culotte.svg", p03), ("04-chemise.svg", p04),
    ("05-chaussettes.svg", p05), ("06-bottes.svg", p06), ("07-lunettes.svg", p07), ("08-j-arrive.svg", p08),
]
