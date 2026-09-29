"""À la claire fontaine — la baignade et le rossignol."""
from base import *
from objets import papillon
from fantastique import personne
from chansons import *

ID = "a-la-claire-fontaine"
FILLETTE = dict(peau="claire", cheveux="roux", coiffure="tresses", habit="#74c0fc", robe=True)


def pre(S, graine=1, haut="#a5d8ff", bas="#fff9db"):
    ciel(S, haut, bas)
    S.add(nuage(150, 120, 0.7), nuage(640, 90, 0.6))
    collines(S, 580, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)
    r = random.Random(graine)
    for _ in range(9):
        S.add(marguerite(r.uniform(20, 780), r.uniform(650, 790), r.uniform(0.5, 0.8), tige=30))


def couverture():
    S = Scene()
    pre(S, 2)
    S.add(chene_branches(640, 640, 0.8))
    S.add(oiseau(750, 305, 0.9, "#a0693a", "#f3dcc3", expr="chante", bec_ouvert=True, flip=True))
    S.add(source(330, 760, 1.2))
    S.add(personne(150, 790, 1.3, expr="content", bras="ouverts", regard=(1, 0), **FILLETTE))
    S.add(envol_notes(560, 300, 380, 200, "#1971c2", 3, 0.8))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#e7f5ff"), rect(0, 220, 400, 50, "#8ce99a"))
    S.add(source(200, 262, 0.6))
    S.add(oiseau(310, 90, 0.6, "#a0693a", "#f3dcc3", expr="chante", bec_ouvert=True, flip=True))
    return S


def p01():
    S = Scene()
    pre(S, 3)
    S.add(source(520, 760, 1.3))
    S.add(personne(200, 790, 1.35, expr="content", bras="salut", regard=(1, 0), **FILLETTE))
    S.add(papillon(360, 300, 0.9))
    return S


def p02():
    S = Scene()
    pre(S, 4)
    S.add(ellipse(400, 700, 330, 80, "#4dabf7"))
    S.add(personne(400, 820, 1.3, expr="rire", bras="haut", **FILLETTE))
    S.add(el("path", d="M 70 700 A 330 80 0 0 0 730 700 L 730 800 L 70 800 Z", fill="#74c0fc", opacity=0.92))
    S.add(eclaboussure(400, 690, 1.3, "#d0ebff"))
    S.add(coeur(240, 330, 0.9, "#ff8787"), coeur(580, 300, 0.7, "#ff8787"))
    return S


def p03():
    S = Scene()
    pre(S, 5)
    S.add(chene_branches(400, 640, 1.0))
    S.add(personne(330, 790, 1.2, expr="dort", bras="calin", **FILLETTE))
    S.add(rect(460, 700, 150, 70, "#ffc9c9", rx=10), rect(460, 720, 150, 14, "#fff", rx=4))
    S.add(soleil(90, 90, 50))
    return S


def p04():
    S = Scene()
    ciel(S, "#a5d8ff", "#e7f5ff")
    S.add(chemin("M -20 520 Q 300 460 820 380", stroke="#8d5524", sw=46))
    S.add(cercle(-40, 300, 200, "#2f9e44"), cercle(860, 240, 200, "#40c057"), cercle(820, 600, 180, "#2f9e44"))
    S.add(oiseau(420, 470, 2.2, "#a0693a", "#f3dcc3", expr="chante", bec_ouvert=True))
    S.add(envol_notes(540, 200, 760, 90, "#1971c2", 4, 1.0))
    return S


def p05():
    S = Scene()
    pre(S, 6, "#ffc9c9", "#fff3bf")
    S.add(soleil(620, 600, 90, "#ff922b", rayons=False))
    sol(S, 620, "#8ce99a", couleur2="#69db7c", y2=730)
    S.add(personne(260, 790, 1.35, expr="chante", bras="donne", regard=(1, 0), **FILLETTE))
    S.add(oiseau(520, 450, 1.1, "#a0693a", "#f3dcc3", expr="chante", bec_ouvert=True, flip=True, pattes=False, ailes="haut"))
    S.add(envol_notes(300, 380, 480, 180, "#c92a2a", 4, 0.9))
    S.add(coeur(640, 260, 0.8, "#fa5252"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-la-fontaine.svg", p01), ("02-baignee.svg", p02), ("03-sous-le-chene.svg", p03),
    ("04-le-rossignol.svg", p04), ("05-refrain.svg", p05),
]
