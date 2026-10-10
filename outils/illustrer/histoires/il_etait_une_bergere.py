"""Il était une bergère, et ron, ron, ron, petit patapon — et le chat fripon."""
from base import *
from fables import fromage, pot_lait, baton
from fantastique import personne
from chansons import *

ID = "il-etait-une-bergere"
BERGERE = dict(peau="rosee", cheveux="chatain", coiffure="tresses", habit="#f783ac", robe=True, acc=("fleur",), couleur_acc="#ffd43b")
CHAT = dict(couleur="#868e96")


def pre(S, graine=1):
    ciel(S, "#a5d8ff", "#fff0f6")
    S.add(nuage(150, 110, 0.7), nuage(640, 80, 0.8))
    collines(S, 560, "#b2f2bb", graine=graine)
    sol(S, 600, "#8ce99a", couleur2="#69db7c", y2=720)


def cuisine(S):
    interieur(S, "#fff4e6", "#e8c39e", 560, papier="#ffe8cc")
    S.add(fenetre(80, 140, 160, 150, rideaux="#f783ac"))
    S.add(table(470, 690, 420, 140, nappe="#ffdeeb"))


def bergere(x, y, s=1.0, **k):
    return personne(x, y, s, **BERGERE, **k)


def chat(x, y, s=1.0, **k):
    return perso("chat", x, y, s, **CHAT, **k)


def couverture():
    S = Scene()
    pre(S, 2)
    for k, x in enumerate((470, 600, 720)):
        S.add(mouton_pre(x, 760 + (k % 2) * 20, 0.9, flip=True))
    S.add(bergere(260, 790, 1.4, expr="chante", bras="tient", objet=baton(68, -146, 80, 20, "#a0693a", 8)))
    S.add(envol_notes(330, 330, 620, 230, "#f783ac"))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, "#fff0f6"))
    S.add(fromage(160, 220, 1.0))
    S.add(perso("chat", 290, 260, 0.45, expr="malin", **CHAT))
    return S


def p01():
    S = Scene()
    pre(S, 3)
    for k, x in enumerate((130, 560, 690)):
        S.add(mouton_pre(x, 760 + (k % 2) * 20, 0.9, flip=k > 0))
    S.add(bergere(360, 790, 1.4, expr="content", bras="bas"))
    S.add(texte(400, 200, "Ron, ron, ron !", 60, "#f783ac", contour="#fff"))
    return S


def p02():
    S = Scene()
    cuisine(S)
    S.add(pot_lait(380, 540, 1.0), fromage(560, 548, 1.3))
    S.add(bergere(180, 800, 1.3, expr="fier", bras="montre", regard=(1, 0)))
    return S


def p03():
    S = Scene()
    cuisine(S)
    S.add(fromage(470, 548, 1.3))
    S.add(chat(680, 800, 1.1, expr="malin", regard=(-1, 0)))
    S.add(texte(680, 420, "Miam ?", 50, "#f783ac", contour="#fff"))
    return S


def p04():
    S = Scene()
    cuisine(S)
    S.add(fromage(470, 548, 1.3))
    S.add(bergere(200, 800, 1.3, expr="fache", bras="montre", regard=(1, 0)))
    S.add(chat(680, 800, 1.0, expr="oups", regard=(-1, 0)))
    return S


def p05():
    S = Scene()
    cuisine(S)
    S.add(fromage(470, 548, 1.3))
    S.add(chat(470, 600, 0.75, expr="miam", bras="haut"))
    S.add(bergere(160, 800, 1.2, expr="surpris", bras="joues"))
    S.add(texte(620, 260, "Le menton !", 54, "#f783ac", contour="#fff"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-la-bergere.svg", p01), ("02-le-fromage.svg", p02), ("03-le-chat.svg", p03),
    ("04-la-patte.svg", p04), ("05-le-menton.svg", p05),
]
