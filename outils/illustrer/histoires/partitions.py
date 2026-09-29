"""Couverture et vignette du livret de partitions (toutes les chansons, notes et paroles)."""
import math

from base import *
from fantastique import personne
from chansons import *

ID = "partitions"


def portee_ondulee(x0, x1, y, amplitude=40, ecart=14, couleur="#5f3dc4", sw=3.5):
    """Cinq lignes de portée qui ondulent comme un ruban."""
    lignes = []
    for k in range(5):
        pts = []
        for i in range(41):
            x = x0 + (x1 - x0) * i / 40
            yy = y + k * ecart + math.sin(i / 40 * math.pi * 2) * amplitude
            pts.append(f"{'M' if i == 0 else 'L'} {n(x)} {n(yy)}")
        lignes.append(chemin(" ".join(pts), stroke=couleur, sw=sw))
    return g(lignes)


def notes_sur_portee(x0, x1, y, amplitude=40, ecart=14, couleur="#5f3dc4", hauteurs=(4, 2, 3, 1, 2, 0, 3)):
    """Des noires posées sur la portée ondulée."""
    m = []
    for i, h in enumerate(hauteurs):
        t = (i + 0.7) / (len(hauteurs) + 0.4)
        x = x0 + (x1 - x0) * t
        yy = y + (4 - h) * ecart + math.sin(t * math.pi * 2) * amplitude - ecart / 2
        m.append(ellipse(x, yy, 11, 8, couleur, rot=-20))
        m.append(trait(x + 9, yy - 2, x + 9, yy - 44, couleur, 4))
    return g(m)


def couverture():
    S = Scene()
    ciel(S, "#ffd8a8", "#fff4e6")
    S.add(soleil(660, 360, 50, "#ffd43b", visage=True))
    S.add(nuage(150, 360, 0.9), nuage(470, 330, 0.6))
    collines(S, 640, "#b2f2bb", graine=5)
    sol(S, 660, "#8ce99a", couleur2="#69db7c", y2=740)
    S.add(portee_ondulee(40, 760, 450, amplitude=30), notes_sur_portee(40, 760, 450, amplitude=30))
    S.add(personne(230, 790, 1.15, peau="claire", cheveux="roux", coiffure="tresses", habit="#ff8787",
                   expr="chante", bras="ouverts"))
    S.add(oiseau(560, 700, 1.3, couleur="#4dabf7", expr="chante", ailes="haut"))
    S.add(envol_notes(300, 560, 520, 470, "#5f3dc4", 4, 0.9, graine=5))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff4e6", rx=0))
    S.add(portee_ondulee(20, 380, 95, amplitude=20, ecart=12, sw=3),
          notes_sur_portee(20, 380, 95, amplitude=20, ecart=12, hauteurs=(4, 2, 3, 1, 0)))
    S.add(etoile5(350, 40, 16, "#fcc419"), etoile5(40, 225, 12, "#fcc419"))
    return S


IMAGES = [("couverture.svg", couverture), ("vignette.svg", vignette)]
