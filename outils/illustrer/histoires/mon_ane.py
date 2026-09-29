"""Mon âne, mon âne a bien mal à la tête — et Madame le soigne."""
from base import *
from objets import barriere
from fantastique import personne
from chansons import *

ID = "mon-ane"
MADAME = dict(peau="rosee", cheveux="gris", coiffure="chignon", habit="#9775fa", robe=True)
LILAS = "#b197fc"
BONNET = dict(acc=("bonnet",), couleur_acc="#fa5252")


def champ(S, graine=1):
    ciel(S, "#a5d8ff", "#fff4e6")
    S.add(nuage(160, 110, 0.7), nuage(620, 90, 0.6))
    collines(S, 580, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)
    S.add(barriere(620, 640, 0.9, largeur=260))


def souliers(x, y, s=1.0):
    return g([ellipse(x - 30 * s, y - 6 * s, 26 * s, 14 * s, LILAS), ellipse(x + 30 * s, y - 6 * s, 26 * s, 14 * s, LILAS)])


def boucles(x, y, s=1.0):
    return g([cercle(x + sgn * 62 * s, y - 158 * s, 10 * s, OR, stroke="#f59f00", stroke_width=3) for sgn in (-1, 1)])


def lunettes_bleues(x, y, s=1.0):
    bleu = "#1c7ed6"
    return place([cercle(-19, -152, 16, "#a5d8ff", opacity=0.55, stroke=bleu, stroke_width=4),
                  cercle(19, -152, 16, "#a5d8ff", opacity=0.55, stroke=bleu, stroke_width=4),
                  trait(-3, -152, 3, -152, bleu, 4)], x, y, s)


def ane(x, y, s, bonnet=False, lunettes=False, **k):
    dessin = perso("ane", x, y, s, acc=("bonnet",) if bonnet else (), couleur_acc="#fa5252" if bonnet else None, **k)
    return g([dessin, lunettes_bleues(x, y, s)]) if lunettes else dessin


def couverture():
    S = Scene()
    champ(S, 2)
    S.add(ane(420, 790, 1.5, bonnet=True, expr="content"), souliers(420, 795, 1.5), boucles(420, 790, 1.5))
    S.add(personne(180, 790, 1.2, expr="content", bras="donne", regard=(1, 0), **MADAME))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff4e6"), rect(0, 230, 400, 40, "#8ce99a"))
    S.add(ane(200, 262, 0.85, bonnet=True, expr="content"))
    return S


def p01():
    S = Scene()
    champ(S, 3)
    S.add(ane(400, 790, 1.6, expr="triste", bras="tete"))
    S.add(eclat(400, 400, 0.8, "#fa5252"))
    return S


def p02():
    S = Scene()
    champ(S, 4)
    S.add(ane(470, 790, 1.5, bonnet=True, expr="rire", bras="haut"), souliers(470, 795, 1.5))
    S.add(personne(180, 790, 1.2, expr="content", bras="hanches", **MADAME))
    S.add(paillettes(640, 330, 1.0))
    return S


def p03():
    S = Scene()
    champ(S, 5)
    S.add(ane(400, 790, 1.6, bonnet=True, expr="pleure", bras="joues"), souliers(400, 795, 1.6))
    return S


def p04():
    S = Scene()
    champ(S, 6)
    S.add(ane(470, 790, 1.5, bonnet=True, expr="content", bras="bas"), souliers(470, 795, 1.5), boucles(470, 790, 1.5))
    S.add(personne(180, 790, 1.2, expr="rire", bras="ouverts", **MADAME))
    S.add(eclat(470 - 93, 553, 0.5), eclat(470 + 93, 553, 0.5))
    return S


def p05():
    S = Scene()
    champ(S, 7)
    S.add(ane(400, 790, 1.6, bonnet=True, expr="inquiet", bras="yeux"), souliers(400, 795, 1.6), boucles(400, 790, 1.6))
    return S


def p06():
    S = Scene()
    champ(S, 8)
    S.add(ane(470, 790, 1.5, bonnet=True, lunettes=True, expr="fier", bras="haut"), souliers(470, 795, 1.5),
          boucles(470, 790, 1.5))
    S.add(personne(180, 790, 1.2, expr="rire", bras="haut", **MADAME))
    S.add(texte(400, 150, "La, la !", 64, "#7048e8", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-mal-a-la-tete.svg", p01), ("02-un-bonnet.svg", p02), ("03-mal-aux-oreilles.svg", p03),
    ("04-boucles-d-oreilles.svg", p04), ("05-mal-aux-yeux.svg", p05), ("06-lunettes-bleues.svg", p06),
]
