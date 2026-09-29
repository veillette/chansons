"""Savez-vous planter les choux ? — avec le doigt, le pied, le genou, le coude, le nez."""
from base import *
from contes import chou
from fantastique import personne
from chansons import *

ID = "savez-vous-planter-les-choux"
JARDINIERE = dict(peau="rosee", cheveux="chatain", coiffure="queue", habit="#fab005", robe=False, jambes="#2b8a3e")


def rangs(S, graine=1):
    r = random.Random(graine)
    for k in range(3):
        for x in range(60 + k * 30, 800, 150):
            S.add(chou(x + r.uniform(-10, 10), 620 + k * 60, 0.6 + k * 0.1))


def couverture():
    S = Scene()
    potager(S, 560, 2)
    rangs(S, 2)
    S.add(personne(260, 790, 1.35, expr="rire", bras="ouverts", **JARDINIERE))
    S.add(perso("lapin", 540, 790, 1.2, expr="miam", bras="porte", objet=chou(0, -50, 0.8)))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff9db"), rect(0, 200, 400, 70, "#a0693a"))
    S.add(chou(130, 230, 1.0), chou(270, 230, 1.0))
    return S


def partie(nom, x, y, texte_x=None, bras="bas", expr="concentre", graine=1, chou_xy=None):
    """Une page : la jardinière plante un chou avec `nom`, repéré par un éclat en (x, y)."""
    def dessin():
        S = Scene()
        potager(S, 560, graine)
        rangs(S, graine)
        S.add(personne(380, 790, 1.5, expr=expr, bras=bras, **JARDINIERE))
        cx, cy = chou_xy or (x + 60, y + 30)
        S.add(chou(cx, cy, 1.5), eclat(x, y, 1.3, "#fa5252"))
        S.add(texte(texte_x or 400, 110, f"Avec {nom} !", 60, "#2b8a3e", contour="#fff"))
        return S
    return dessin


def p01():
    S = Scene()
    potager(S, 560, 3)
    rangs(S, 3)
    S.add(personne(200, 790, 1.3, expr="rire", bras="haut", **JARDINIERE))
    S.add(perso("lapin", 420, 790, 1.1, expr="rire", bras="haut"))
    S.add(perso("cochon", 620, 790, 1.1, expr="rire", bras="haut"))
    S.add(texte(400, 120, "À la mode de chez nous !", 44, "#e67700", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-savez-vous.svg", p01),
    ("02-le-doigt.svg", partie("le doigt", 509, 595, bras="montre", chou_xy=(540, 700))),
    ("03-le-pied.svg", partie("le pied", 420, 780, graine=4, chou_xy=(520, 770))),
    ("04-le-genou.svg", partie("le genou", 402, 735, graine=5, chou_xy=(520, 740), bras="large")),
    ("05-le-coude.svg", partie("le coude", 479, 679, graine=6, bras="hanches", chou_xy=(560, 740))),
    ("06-le-nez.svg", partie("le nez", 380, 578, graine=7, bras="ouverts", expr="rire", chou_xy=(510, 600))),
]
