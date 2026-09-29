"""Une souris verte — qui courait dans l'herbe."""
from base import *
from objets import *
from fantastique import personne
from chansons import *

ID = "une-souris-verte"
ENFANT = dict(peau="doree", cheveux="brun", coiffure="queue", habit="#ffd43b", robe=False, jambes="#1971c2")
MONSIEUR1 = dict(peau="claire", cheveux="gris", barbe="#ced4da", habit="#364fc7")
MONSIEUR2 = dict(peau="brune", cheveux="noir", habit="#862e9c", acc=("lunettes",))


def pre(S, graine=1):
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(nuage(160, 140, 0.8), nuage(620, 110, 0.6))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=700)
    r = random.Random(graine)
    for _ in range(26):
        S.add(herbe(r.uniform(0, 800), r.uniform(620, 790), r.uniform(0.6, 1.1)))


def souris_pendue(x, y, s=1.0, expr="surpris"):
    """La souris tenue par la queue, tête en bas ; (x, y) = bout de la queue."""
    return g([chemin(f"M {x} {y} Q {x + 20 * s} {y + 40 * s} {x} {y + 70 * s}", stroke="#ffa8a8", sw=5),
              place(souris_verte(0, 0, 0.7, expr=expr, bras="haut"), x, y + 70 * s, s, rot=180)])


def couverture():
    S = Scene()
    pre(S, 2)
    S.add(fleur(120, 700, 1.2, "#ff6b6b"), fleur(690, 690, 1.0, "#cc5de8"), fleur(610, 740, 0.8, "#ffd43b"))
    S.add(souris_verte(400, 780, 1.7, expr="rire", bras="salut"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"), rect(0, 210, 400, 60, "#8ce99a"))
    S.add(souris_verte(200, 262, 0.95, expr="rire", bras="salut"))
    return S


def p01():
    S = Scene()
    pre(S, 3)
    S.add(souris_verte(420, 760, 1.3, expr="rire", bras="course", rot=-8))
    S.add(mouvement(230, 560, 1.4), mouvement(220, 640, 1.2))
    S.add(papillon(640, 320, 1.2), coccinelle(150, 740, 1.2))
    return S


def p02():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(nuage(160, 140, 0.8), nuage(620, 110, 0.6))
    sol(S, 700, "#8ce99a", couleur2="#69db7c", y2=760)
    S.add(danseur(540, 790, 1.45, **MONSIEUR1, bras="hanches", regard=(-1, 0)))
    S.add(danseur(710, 790, 1.35, **MONSIEUR2, bras="croises", regard=(-1, 0), chapeau_=False))
    S.add(personne(200, 790, 1.7, expr="fier", bras="haut", **ENFANT))
    mg, md = mains(200, 790, 1.7, "haut")
    S.add(souris_pendue(md[0], md[1] - 20, 1.25, expr="oups"))
    return S


def p03():
    S = Scene()
    pre(S, 5)
    S.add(danseur(200, 780, 1.3, **MONSIEUR1, bras="montre", expr="malin", regard=(1, 0)))
    S.add(poele(540, 540, 1.0))
    S.add(bol(700, 600, 0.9, "#74c0fc", "#a5d8ff", cuillere=False))
    S.add(escargot(560, 780, 1.4, coquille="#f59f00", corps="#8ce99a", expr="rire"))
    S.add(chemin("M 520 560 q -10 -30 0 -60 q 10 -30 0 -60", stroke="#adb5bd", sw=6, opacity=0.7))
    S.add(chemin("M 600 560 q -10 -30 0 -60 q 10 -30 0 -60", stroke="#adb5bd", sw=6, opacity=0.7))
    S.add(bulle(560, 150, 380, 100, "Trempez-la\ndans l'huile !", 36, pointe=(300, 400)))
    return S


def p04():
    S = Scene()
    interieur(S, "#fff4e6", "#c9a47e", 600, papier="#ffe8cc")
    S.add(tiroir(400, 770, 1.4, dedans=g([ellipse(0, -205, 180, 30, "#212529"),
                                           ellipse(-24, -216, 12, 9, "#ffe066"), ellipse(24, -216, 12, 9, "#ffe066"),
                                           cercle(-24, -216, 4, ENCRE), cercle(24, -216, 4, ENCRE)])))
    S.add(bulle(560, 170, 380, 100, "Il fait\ntrop noir !", 38, pointe=(430, 380)))
    return S


def p05():
    S = Scene()
    pre(S, 6)
    S.add(soleil(640, 150, 70, visage=True))
    S.add(personne(260, 780, 1.4, expr="rire", bras="donne", regard=(1, 0), **ENFANT))
    S.add(chapeau_haut(520, 730, 1.6, "#495057", "#fa5252"))
    S.add(ellipse(520, 538, 86, 18, "#212529"))
    S.add(souris_verte(520, 640, 0.9, expr="oups", bras="tete"))
    S.add(rect(430, 545, 180, 150, "#495057"), rect(430, 676, 180, 32, "#fa5252"))
    S.add(goutte(440, 380, 1.2, "#74c0fc"), goutte(610, 360, 1.0, "#74c0fc"))
    S.add(bulle(300, 150, 380, 100, "Il fait\ntrop chaud !", 38, pointe=(500, 420)))
    return S


def p06():
    S = Scene()
    pre(S, 7)
    S.add(personne(300, 780, 1.5, expr="bouche_bee", bras="haut", **ENFANT))
    S.add(souris_verte(620, 780, 1.0, expr="malin", bras="salut", regard=(-1, 0)))
    S.add(mouvement(720, 640, 1.2, rot=180))
    for k in range(3):
        S.add(cercle(420 + k * 30, 770 - (k % 2) * 10, 11, "#8d5524"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-dans-l-herbe.svg", p01), ("02-par-la-queue.svg", p02), ("03-escargot.svg", p03),
    ("04-tiroir.svg", p04), ("05-chapeau.svg", p05), ("06-culotte.svg", p06),
]
