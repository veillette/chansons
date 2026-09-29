"""Au clair de la lune — Lubin, Pierrot, la plume et la chandelle."""
from base import *
from fantastique import personne
from chansons import *

ID = "au-clair-de-la-lune"
NUIT_HAUT, NUIT_BAS = "#1c2a52", "#4c5b9a"
LUBIN = dict(peau="doree", cheveux="brun", coiffure="herisses", habit="#f08c00", robe=False, jambes="#5c3a1e")
VOISINE = dict(peau="rosee", cheveux="roux", coiffure="chignon", habit="#e64980", robe=True)


def rue(S, graine=1, lune_x=620, lune_y=140):
    nuit(S, NUIT_HAUT, NUIT_BAS)
    etoiles(S, 34, graine, (0, 0, 800, 420))
    S.add(lune(lune_x, lune_y, 70, visage=True))
    for x, h, c in [(-20, 300, "#364fc7"), (160, 360, "#3b5bdb"), (560, 330, "#364fc7"), (720, 280, "#3b5bdb")]:
        S.add(rect(x, 640 - h, 160, h, c))
        S.add(poly([(x - 10, 640 - h), (x + 80, 580 - h), (x + 170, 640 - h)], "#1c2a52"))
        for k in range(2):
            S.add(rect(x + 30 + k * 60, 690 - h, 36, 44, "#ffe066" if (x + k) % 3 else "#1c2a52"))
    S.add(rect(0, 640, 800, 160, "#5c677d"))
    for k in range(9):
        S.add(rect(k * 100 - (k % 2) * 40, 700 + (k % 3) * 30, 70, 16, "#6c7a91", rx=6))


def couverture():
    S = Scene()
    rue(S, 2, 560, 230)
    S.add(pierrot(260, 770, 1.6, expr="sourire", bras="salut", regard=(1, -1)))
    S.add(envol_notes(420, 520, 740, 400, "#fff3bf", 4, 0.9))
    return S


def vignette():
    S = Scene(400, 270)
    S.add(rect(0, 0, 400, 270, NUIT_HAUT), lune(300, 90, 50, visage=True))
    S.add(pierrot(150, 262, 0.95, bras="salut", regard=(1, -1)))
    return S


def p01():
    S = Scene()
    rue(S, 3)
    S.add(personne(330, 770, 1.6, expr="triste", bras="donne", regard=(1, 0), objet=chandelle(84, -80, 0.8, allumee=False), **LUBIN))
    S.add(plume(640, 560, 1.2, rot=20))
    S.add(pensee(640, 470, 70, "", depuis=(470, 520)))
    S.add(plume(640, 510, 0.6, rot=30))
    return S


def p02():
    S = Scene()
    nuit(S, NUIT_HAUT, NUIT_BAS)
    etoiles(S, 20, 4, (0, 0, 800, 200))
    S.add(lune(120, 110, 55, visage=True))
    porte_maison(S, 520, 720, couleur="#1098ad", mur="#e5dbff", toit="#5f3dc4")
    S.add(rect(0, 720, 800, 80, "#5c677d"))
    S.add(personne(200, 780, 1.4, expr="inquiet", bras="montre", regard=(1, 0), objet=chandelle(-60, -60, 0.6, allumee=False), **LUBIN))
    S.add(texte(350, 470, "toc", 50, "#5f3dc4", rot=-12), texte(370, 540, "toc !", 50, "#5f3dc4", rot=8))
    return S


def p03():
    S = Scene()
    interieur(S, "#5f3dc4", "#4a3b8f", 600, papier="#7048e8", plinthe="#3b2f7a")
    S.add(fenetre(80, 90, 200, 180, NUIT_HAUT, cadre="#dbe4ff", nuit_=True, rideaux="#fcc419"))
    S.add(lit(480, 760, 480, couverture="#f8f9fa", bois="#c68642"))
    S.add(pierrot(360, 680, 1.0, expr="dort", bras="bas"))
    S.add(rect(230, 610, 480, 100, "#f8f9fa", rx=20))
    S.add(zzz(470, 360, 1.3, "#fff3bf"))
    return S


def p05():
    S = Scene()
    rue(S, 5, 150, 120)
    S.add(maison(560, 640, 1.3, mur="#ffe8cc", toit="#c92a2a", lumiere=True))
    S.add(chemin("M 632 330 Q 640 280 620 240 Q 600 200 630 160", stroke="#ced4da", sw=10, opacity=0.6))
    S.add(pierrot(300, 780, 1.3, bras="montre", regard=(1, 0)))
    S.add(personne(130, 780, 1.2, expr="content", regard=(1, 0), **LUBIN))
    return S


def p06():
    S = Scene()
    interieur(S, "#fff4e6", "#c68642", 600, papier="#ffe8cc")
    S.add(rect(520, 330, 200, 270, "#495057"), rect(540, 470, 160, 130, "#343a40"))
    S.add(chemin("M 580 600 Q 560 520 600 480 Q 610 530 630 500 Q 650 540 660 480 Q 700 530 670 600 Z", "#ff922b"))
    S.add(chemin("M 600 600 Q 600 550 620 530 Q 630 560 650 540 Q 660 570 650 600 Z", "#ffe066"))
    S.add(personne(330, 770, 1.6, expr="rire", bras="salut", **VOISINE))
    S.add(eclat(610, 470, 0.9))
    return S


def p07():
    S = Scene()
    nuit(S, NUIT_HAUT, NUIT_BAS)
    etoiles(S, 20, 6, (0, 0, 800, 200))
    S.add(lune(660, 110, 55, visage=True))
    porte_maison(S, 400, 720, couleur="#e03131", mur="#ffe8cc", toit="#c92a2a", ouverte=True, lumiere=True)
    S.add(rect(0, 720, 800, 80, "#5c677d"))
    S.add(personne(160, 780, 1.3, expr="timide", bras="montre", regard=(1, 0), **LUBIN))
    S.add(personne(400, 740, 1.1, expr="surpris", bras="hanches", **VOISINE))
    S.add(bulle(620, 330, 280, 110, "Qui frappe\nde la sorte ?", 32, pointe=(460, 440)))
    return S


def p08():
    S = Scene()
    interieur(S, "#fff4e6", "#c68642", 600, papier="#ffe8cc")
    S.add(fenetre(520, 100, 200, 170, NUIT_HAUT, cadre="#fff", nuit_=True))
    S.add(personne(260, 770, 1.4, expr="content", bras="donne", regard=(1, 0), objet=chandelle(84, -60, 0.7), **LUBIN))
    S.add(personne(540, 770, 1.4, expr="rire", bras="donne", flip=True, regard=(-1, 0), **VOISINE))
    S.add(coeur(400, 300, 1.2), coeur(460, 240, 0.7, "#ff8787"))
    return S


IMAGES = [
    ("couverture.svg", couverture), ("vignette.svg", vignette),
    ("01-plume.svg", p01), ("02-porte.svg", p02), ("03-dans-son-lit.svg", p03),
    ("04-la-voisine.svg", p05), ("05-le-briquet.svg", p06), ("06-qui-frappe.svg", p07), ("07-ouvrez.svg", p08),
]
