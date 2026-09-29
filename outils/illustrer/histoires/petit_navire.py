"""Il était un petit navire — le mousse sauvé par les petits poissons."""
from base import *
from fantastique import personne
from chansons import *

ID = "petit-navire"
CAPITAINE = dict(peau="rosee", cheveux="gris", barbe="#e9ecef", coiffure="courts", habit="#1864ab", robe=False, jambes="#212529")
MARIN = dict(peau="brune", cheveux="noir", coiffure="courts", habit="#f8f9fa", robe=False, jambes="#1c7ed6")


def equipage(expr_c="sourire", expr_m="sourire", expr_mousse="rire", bras_mousse="salut", objet=None):
    return [personne(-120, -60, 0.55, expr=expr_c, **CAPITAINE),
            personne(0, -60, 0.55, expr=expr_m, **MARIN),
            mousse(110, -60, 0.5, expr=expr_mousse, bras=bras_mousse, objet=objet)]


def couverture():
    S = Scene()
    mer(S, 540)
    S.add(soleil(130, 130, 55))
    S.add(navire(420, 640, 1.2, marins=equipage()))
    S.add(vagues_devant(650))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 200, "#a5d8ff"), rect(0, 200, 400, 70, "#1c7ed6"))
    S.add(navire(200, 215, 0.52))
    return S


def p01():
    S = Scene()
    mer(S, 560)
    S.add(rect(0, 520, 260, 60, "#c68642"), rect(20, 580, 20, 200, "#8d5524"), rect(200, 580, 20, 200, "#8d5524"))
    S.add(navire(470, 620, 1.1, marins=equipage(expr_mousse="content")))
    S.add(vagues_devant(640))
    S.add(texte(470, 110, "Tout neuf !", 50, "#c92a2a", contour="#fff"))
    return S


def p02():
    S = Scene()
    mer(S, 480, "#4dabf7", "#d0ebff")
    S.add(soleil(680, 110, 50))
    S.add(navire(360, 600, 1.0, penche=-4, marins=equipage(bras_mousse="haut")))
    S.add(vagues_devant(610))
    for x, y in [(620, 240), (700, 280)]:
        S.add(oiseau(x, y, 0.5, "#f8f9fa", "#ffffff", ailes="haut", pattes=False))
    return S


def p03():
    S = Scene()
    interieur(S, "#c68642", "#8d5524", 600, plinthe="#5c3a1e")
    for k in range(9):
        S.add(trait(0, k * 70, 800, k * 70, "#a0693a", 4))
    S.add(cercle(640, 190, 60, "#a5d8ff", stroke="#ffd43b", stroke_width=14))
    S.add(el("rect", x=320, y=480, width=160, height=200, fill="#a0693a", rx=30))
    S.add(ellipse(400, 480, 80, 20, "#5c3a1e"))
    S.add(personne(190, 780, 1.3, expr="triste", bras="ouverts", **CAPITAINE))
    S.add(mousse(610, 780, 1.2, expr="inquiet", bras="bouche"))
    S.add(texte(400, 420, "vide !", 44, "#fff4e6"))
    return S


def p04():
    S = Scene()
    mer(S, 600, "#ffa94d", "#ffe8cc")
    S.add(personne(400, 780, 1.6, expr="malin", bras="donne", regard=(1, 0), **CAPITAINE))
    mg, md = mains(400, 780, 1.6, "donne")
    for k in range(4):
        S.add(paille(md[0] - 12 + k * 10, md[1] + 10, 1.2, rot=-8 + k * 5))
    S.add(personne(120, 780, 1.1, expr="inquiet", flip=True, **MARIN))
    S.add(mousse(680, 780, 1.1, expr="inquiet", regard=(-1, 0)))
    return S


def p05():
    S = Scene()
    mer(S, 600, "#ffa94d", "#ffe8cc")
    S.add(mousse(400, 780, 1.8, expr="pleure", bras="montre", larmes=True))
    mg, md = mains(400, 780, 1.8, "montre")
    S.add(paille(md[0], md[1] + 10, 1.6, longue=False))
    S.add(personne(120, 780, 1.1, expr="oups", **CAPITAINE))
    S.add(personne(690, 780, 1.1, expr="surpris", **MARIN))
    return S


def p06():
    S = Scene()
    mer(S, 520)
    S.add(navire(420, 620, 1.1, marins=equipage(expr_c="bouche_bee", expr_m="rire", expr_mousse="rire", bras_mousse="haut")))
    S.add(vagues_devant(640))
    r = random.Random(3)
    for k in range(9):
        S.add(poisson(r.uniform(80, 720), r.uniform(120, 420), r.uniform(0.7, 1.0), r.choice(["#ff922b", "#fcc419", "#ff6b6b", "#74c0fc"]),
                      expr="rire", rot=r.uniform(-40, 40), flip=r.random() < 0.5))
    return S


def p07():
    S = Scene()
    mer(S, 600)
    S.add(rect(0, 600, 800, 200, "#a0693a"))
    for k in range(5):
        S.add(trait(0, 620 + k * 40, 800, 620 + k * 40, "#8d5524", 4))
    S.add(poele(400, 560, 1.4))
    for k in range(3):
        S.add(poisson(360 + k * 40, 550, 0.4, "#ffa94d", expr="dort", rot=10))
    S.add(personne(160, 780, 1.2, expr="miam", **CAPITAINE))
    S.add(mousse(640, 780, 1.3, expr="rire", bras="haut"))
    S.add(chemin("M 380 500 q -10 -30 0 -60 q 10 -30 0 -60", stroke="#ced4da", sw=6, opacity=0.8))
    return S


def p08():
    S = Scene()
    mer(S, 540, "#ffa94d", "#ffe8cc")
    S.add(soleil(620, 520, 90, "#ff922b", rayons=False))
    S.add(navire(340, 640, 1.0, marins=equipage(expr_c="rire", expr_m="rire", bras_mousse="salut")))
    S.add(vagues_devant(650, "#d9480f", "#ff922b"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-petit-navire.svg", p01), ("02-voyage.svg", p02), ("03-les-vivres.svg", p03), ("04-courte-paille.svg", p04),
    ("05-le-plus-jeune.svg", p05), ("06-les-poissons.svg", p06), ("07-a-frire.svg", p07), ("08-recommencer.svg", p08),
]
