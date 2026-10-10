"""En passant par la Lorraine, avec mes sabots — et un bouquet de marjolaine."""
from base import *
from fantastique import personne, princesse
from chansons import *

ID = "en-passant-par-la-lorraine"
FILLE = dict(peau="rosee", cheveux="blond", coiffure="tresses", habit="#4dabf7", robe=True, acc=("noeud",), couleur_acc="#fa5252")
CAPITAINES = [dict(habit="#1c7ed6"), dict(habit="#c92a2a"), dict(habit="#2b8a3e")]
PRINCE = dict(peau="doree", cheveux="brun", coiffure="courts", habit="#7048e8", robe=False, jambes="#f8f9fa",
              acc=("couronne",), cape="#c92a2a")


def fille(x, y, s=1.0, sabots=True, **k):
    dessin = personne(x, y, s, **FILLE, **k)
    if not sabots:
        return dessin
    return g([dessin, sabot(x - 40 * s, y + 2 * s, 0.36 * s, flip=True), sabot(x + 40 * s, y + 2 * s, 0.36 * s)])


def capitaine(x, y, s=1.0, habit="#1c7ed6", **k):
    return g([personne(x, y, s, peau="doree", cheveux="brun", coiffure="courts", habit=habit, robe=False, jambes="#f8f9fa",
                       ceinture="#f59f00", **k),
              place([chemin("M -70 -196 Q 0 -260 70 -196 Q 0 -214 -70 -196 Z", "#343a40"), cercle(0, -226, 9, "#fa5252")], x, y, s)])


def route(S, graine=1):
    ciel(S, "#a5d8ff", "#fff9db")
    S.add(nuage(150, 110, 0.7), nuage(640, 80, 0.8))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)
    S.add(chemin("M 330 600 Q 300 700 160 800 L 640 800 Q 500 700 470 600 Z", "#e9d8b4"))


def couverture():
    S = Scene()
    route(S, 2)
    for k, x in enumerate((560, 650, 740)):
        S.add(capitaine(x, 650, 0.6, CAPITAINES[k]["habit"], expr="sourire", bras="salut"))
    S.add(fille(300, 790, 1.45, expr="rire", bras="salut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"))
    S.add(sabot(150, 200, 1.0, flip=True), sabot(260, 200, 1.0))
    S.add(bouquet(200, 110, 0.5))
    return S


def p01():
    S = Scene()
    route(S, 3)
    S.add(fille(400, 790, 1.5, expr="content", bras="bas"))
    S.add(texte(160, 760, "clop", 40, "#a0693a", rot=-10), texte(640, 740, "clop", 40, "#a0693a", rot=10))
    return S


def p02():
    S = Scene()
    route(S, 4)
    for k, x in enumerate((420, 560, 700)):
        S.add(capitaine(x, 790, 1.05, CAPITAINES[k]["habit"], expr="sourire", bras="salut" if k == 1 else "bas", flip=True))
    S.add(fille(160, 800, 1.1, expr="surpris", bras="bas"))
    return S


def p03():
    S = Scene()
    route(S, 5)
    S.add(capitaine(620, 790, 1.0, CAPITAINES[0]["habit"], expr="malin", bras="montre", flip=True))
    S.add(fille(300, 800, 1.45, expr="fache", bras="hanches"))
    return S


def p04():
    S = Scene()
    route(S, 6)
    S.add(personne(560, 790, 1.3, expr="content", bras="donne", flip=True, objet=bouquet(84, -92, 0.6), **PRINCE))
    S.add(fille(250, 800, 1.3, expr="timide", bras="calin"))
    S.add(coeur(400, 260, 1.0, "#ff6b6b"))
    return S


def p05():
    S = Scene()
    route(S, 7)
    S.add(personne(400, 790, 1.5, expr="rire", bras="tient", objet=bouquet(68, -146, 0.75), **dict(FILLE, acc=("couronne",))))
    S.add(paillettes(560, 300, 1.2), paillettes(250, 340, 0.9))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-mes-sabots.svg", p01), ("02-trois-capitaines.svg", p02), ("03-vilaine.svg", p03),
    ("04-la-marjolaine.svg", p04), ("05-je-serai-reine.svg", p05),
]
