"""
Personnages, accessoires et décors des chansons : crocodile, alouette,
petit navire, pont d'Avignon, clocher, plume et chandelle, berceau,
marionnette, portées et notes de musique…

Mêmes conventions que `base.py` : page de 800 × 800 ; (x, y) désigne en
général le point posé au sol (ou sur l'eau).
"""
from base import *
from base import _assombrir
from objets import bougie
from fantastique import personne, OR


# ---------------------------------------------------------------------------
# Musique
# ---------------------------------------------------------------------------

def croche(x, y, s=1.0, couleur=ENCRE, rot=0):
    """Une seule note (croche)."""
    m = [ellipse(0, 0, 11, 8, couleur, rot=-20), trait(9, -2, 9, -42, couleur, 4),
         chemin("M 9 -42 Q 26 -34 24 -16", stroke=couleur, sw=4)]
    return place(m, x, y, s, rot=rot)


def envol_notes(x0, y0, x1, y1, couleur=ENCRE, nb=4, s=0.8, graine=1):
    """Des notes qui s'envolent d'un point vers un autre, en vague."""
    r = random.Random(graine)
    m = []
    for k in range(nb):
        t = (k + 0.5) / nb
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + math.sin(t * math.pi * 2) * 24
        if k % 2:
            m.append(notes(x - 30, y, s * 0.7, couleur))
        else:
            m.append(croche(x, y, s, couleur, rot=r.uniform(-15, 15)))
    return g(m)


# ---------------------------------------------------------------------------
# Au clair de la lune
# ---------------------------------------------------------------------------

def plume(x, y, s=1.0, rot=-30, couleur="#ffffff", bord="#adb5bd"):
    """Plume d'oie pour écrire ; (x, y) = pointe."""
    m = [chemin("M 0 0 Q -6 -60 4 -150 Q 40 -110 30 -40 Q 18 -8 0 0 Z", couleur, stroke=bord, sw=3),
         chemin("M 0 0 Q 8 -70 4 -150", stroke=bord, sw=3)]
    for k in range(5):
        yy = -40 - k * 20
        m.append(trait(6, yy, 22, yy - 12, bord, 2))
    return place(m, x, y, s, rot=rot)


def chandelle(x, y, s=1.0, allumee=True):
    """Bougeoir avec sa chandelle ; (x, y) = dessous du bougeoir."""
    m = [ellipse(0, -6, 44, 12, "#fab005"), rect(-8, -26, 16, 22, "#fab005"),
         chemin("M 40 -10 Q 66 -10 62 -30 Q 58 -44 46 -36", stroke="#fab005", sw=7),
         rect(-14, -110, 28, 86, "#fff9db", rx=4), trait(0, -110, 0, -120, ENCRE, 3)]
    if allumee:
        m += [ellipse(0, -136, 22, 30, "#ffe066", opacity=0.35),
              chemin("M 0 -150 Q 12 -128 0 -118 Q -12 -128 0 -150 Z", "#ff922b"),
              chemin("M 0 -140 Q 5 -128 0 -122 Q -5 -128 0 -140 Z", "#ffe066")]
    else:
        m.append(chemin("M 0 -122 Q -12 -140 2 -156 Q 14 -170 0 -186", stroke="#adb5bd", sw=4, opacity=0.8))
    return place(m, x, y, s)


def pierrot(x, y, s=1.0, **k):
    """Pierrot : habit blanc à gros boutons, collerette et calotte noire."""
    k.setdefault("peau", "claire")
    k.setdefault("cheveux", "noir")
    return personne(x, y, s, habit="#f8f9fa", robe=False, jambes="#f1f3f5", chaussures="#343a40",
                    coiffure="courts", acc=("col",) + tuple(k.pop("acc", ())), **k) + \
        place([cercle(0, -100, 7, ENCRE), cercle(0, -76, 7, ENCRE), cercle(0, -52, 7, ENCRE),
               chemin("M -50 -196 Q 0 -232 50 -196 Q 0 -206 -50 -196 Z", "#343a40")], x, y, s)


def porte_maison(S, x=400, y=720, couleur="#a0522d", mur="#ffe8cc", toit="#c92a2a", ouverte=False, lumiere=False):
    """Façade de maison vue de près, avec une grande porte ; (x, y) = seuil."""
    S.add(rect(x - 260, y - 470, 520, 470, mur))
    S.add(poly([(x - 300, y - 460), (x, y - 640), (x + 300, y - 460)], toit))
    S.add(rect(x - 90, y - 300, 180, 300, "#5c3a1e" if ouverte else couleur, rx=10))
    if ouverte:
        S.add(rect(x - 70, y - 280, 140, 280, "#ffe066" if lumiere else "#343a40"))
        S.add(poly([(x - 90, y - 300), (x - 150, y - 320), (x - 150, y + 20), (x - 90, y)], couleur))
    else:
        for k in range(3):
            S.add(rect(x - 70 + k * 50, y - 280, 40, 260, _assombrir(couleur, 0.9), rx=6))
        S.add(cercle(x + 60, y - 150, 9, "#ffd43b"))
    S.add(rect(x - 110, y - 10, 220, 16, "#adb5bd", rx=4))
    fen = "#ffe066" if lumiere else "#1c2a52"
    for fx in (x - 220, x + 130):
        S.add(rect(fx, y - 390, 90, 90, fen, stroke="#fff", stroke_width=8))
        S.add(trait(fx + 45, y - 390, fx + 45, y - 300, "#fff", 6))


# ---------------------------------------------------------------------------
# Frère Jacques
# ---------------------------------------------------------------------------

def moine(x, y, s=1.0, **k):
    """Un moine en robe de bure, avec sa tonsure."""
    k.setdefault("peau", "rosee")
    k.setdefault("cheveux", "chatain")
    k.setdefault("coiffure", "chauve_cote")
    return personne(x, y, s, habit="#8d5524", robe=True, ceinture="#f1dcc3", **k)


def cloche(x, y, s=1.0, couleur=OR, rot=0, battant=0, ondes=False):
    """Cloche ; (x, y) = point d'attache en haut. `battant` décale le battant."""
    m = [rect(-16, -6, 32, 16, "#868e96", rx=5),
         chemin("M -46 110 Q -46 30 -30 12 Q 0 -8 30 12 Q 46 30 46 110 Q 62 118 62 126 L -62 126 Q -62 118 -46 110 Z",
                couleur, stroke=_assombrir(couleur, 0.75), sw=4),
         chemin("M -24 40 Q -30 70 -30 100", stroke="#fff", sw=6, opacity=0.5),
         trait(0, 20, battant, 126, "#495057", 5), cercle(battant, 132, 11, "#495057")]
    if ondes:
        for k in (1, 2, 3):
            r = 70 + k * 26
            m.append(chemin(f"M {r * 0.9} {40 - k * 6} Q {r * 1.1} 80 {r * 0.9} {130 + k * 8}", stroke=couleur, sw=6, opacity=1 - k * 0.25))
            m.append(chemin(f"M {-r * 0.9} {40 - k * 6} Q {-r * 1.1} 80 {-r * 0.9} {130 + k * 8}", stroke=couleur, sw=6, opacity=1 - k * 0.25))
    return place(m, x, y, s, rot=rot)


def clocher(x, y, s=1.0, mur="#f1e3c8", toit="#5c7cfa", cloche_=True, battant=0, ondes=False):
    """Petite chapelle à clocher ; (x, y) = milieu de la base."""
    m = [rect(-170, -200, 340, 200, mur), poly([(-190, -196), (0, -300), (190, -196)], toit),
         rect(-70, -520, 140, 330, mur), poly([(-90, -516), (0, -680), (90, -516)], toit),
         trait(0, -680, 0, -730, "#495057", 6), trait(-18, -712, 18, -712, "#495057", 6),
         chemin("M -44 -380 L -44 -450 Q 0 -500 44 -450 L 44 -380 Z", "#343a40"),
         chemin("M -40 0 L -40 -90 Q 0 -130 40 -90 L 40 0 Z", "#8d5524"),
         cercle(0, -250, 22, "#a5d8ff", stroke="#fff", stroke_width=5)]
    for fx in (-130, 90):
        m.append(chemin(f"M {fx} -60 L {fx} -120 Q {fx + 20} -144 {fx + 40} -120 L {fx + 40} -60 Z", "#a5d8ff", stroke="#fff", sw=4))
    if cloche_:
        m.append(cloche(0, -470, 0.62, battant=battant, ondes=ondes))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Ah ! les crocodiles
# ---------------------------------------------------------------------------

VERT_CROCO = "#40c057"


def crocodile(x, y, s=1.0, couleur=VERT_CROCO, ventre="#d8f5a2", expr="sourire", gueule=False,
              flip=False, chapeau_=None, tambour=False, larmes=False, marche=0):
    """Crocodile de profil, la tête à droite ; (x, y) = au sol, sous le ventre.

    gueule : grande bouche ouverte pleine de dents ; chapeau_ : couleur d'un
    bicorne de papier ; tambour : petit tambour sur le ventre ;
    marche : décalage des pattes (-1 à 1) pour la marche."""
    fonce = _assombrir(couleur, 0.78)
    m = []
    # queue qui traîne derrière
    m.append(chemin("M -110 -70 Q -210 -60 -300 -10 Q -230 -30 -120 -20 Z", couleur))
    for k in range(5):
        tx = -140 - k * 30
        ty = -54 + k * 8
        m.append(poly([(tx - 12, ty), (tx, ty - 18 + k * 2), (tx + 12, ty)], fonce))
    # pattes arrière (derrière)
    for px, dx in ((-70, -marche * 14), (80, marche * 14)):
        m.append(rect(px - 20 + dx, -50, 38, 50, fonce, rx=14))
    # corps
    m.append(ellipse(0, -80, 130, 62, couleur))
    m.append(chemin("M -110 -60 Q 0 -10 120 -62 Q 0 -30 -110 -60 Z", ventre))
    for k in range(6):
        bx = -90 + k * 34
        m.append(poly([(bx - 13, -134), (bx, -156), (bx + 13, -134)], fonce))
    # pattes avant
    for px, dx in ((-40, marche * 14), (100, -marche * 14)):
        m.append(rect(px - 20 + dx, -48, 40, 48, couleur, rx=14))
        m += [cercle(px - 12 + dx + j * 12, -2, 7, couleur) for j in range(3)]
    if tambour:
        m += [rect(-10, -110, 80, 60, "#fa5252", rx=6), ellipse(30, -110, 40, 10, "#fff4e6", stroke="#c92a2a", stroke_width=3),
              ellipse(30, -50, 40, 10, "#fa5252"), chemin("M -10 -104 L 10 -56 L 30 -104 L 50 -56 L 70 -104", stroke="#ffd43b", sw=4)]
    # tête et long museau
    if gueule:
        m.append(chemin("M 90 -120 Q 170 -190 330 -210 Q 340 -196 320 -186 Q 190 -150 140 -100 Z", couleur))  # mâchoire haute
        m.append(chemin("M 110 -80 Q 200 -60 330 -76 Q 340 -92 320 -98 Q 200 -104 140 -104 Z", couleur))  # mâchoire basse
        m.append(chemin("M 140 -104 Q 220 -170 318 -188 L 318 -98 Q 220 -104 140 -104 Z", "#e03131"))
        m.append(ellipse(230, -110, 50, 12, "#ff8787"))
        for k in range(7):
            tx = 170 + k * 22
            ty = -150 - k * 5
            m.append(poly([(tx - 7, ty), (tx, ty + 16), (tx + 7, ty)], "#fff"))
            m.append(poly([(tx - 7, -100), (tx, -116), (tx + 7, -100)], "#fff"))
        oeil_y, oeil_x = -176, 136
    else:
        m.append(chemin("M 90 -130 Q 150 -160 330 -130 Q 350 -110 330 -90 Q 200 -70 100 -60 Z", couleur))
        m.append(chemin("M 130 -96 Q 230 -100 336 -108", stroke=fonce, sw=4))
        if expr in ("sourire", "content", "rire", "fier", "malin"):
            m.append(chemin("M 150 -96 Q 170 -84 190 -96", stroke=fonce, sw=4))
        for k in range(5):
            tx = 190 + k * 28
            m.append(poly([(tx - 6, -101), (tx, -88), (tx + 6, -101)], "#fff"))
        oeil_y, oeil_x = -150, 136
    m.append(cercle(320, (-196 if gueule else -128), 5, fonce))
    # bosse de l'œil
    ys, bs, ss = EXPRESSIONS[expr]
    m.append(cercle(oeil_x, oeil_y, 30, couleur))
    m.append(oeil(oeil_x + 4, oeil_y - 2, ys, (1, 0), sclere=True, taille=1.1))
    if ss == "faches":
        m.append(trait(oeil_x - 16, oeil_y - 30, oeil_x + 22, oeil_y - 18, ENCRE, 5))
    elif ss in ("tristes", "hauts"):
        m.append(trait(oeil_x - 14, oeil_y - 24, oeil_x + 20, oeil_y - 34 if ss == "hauts" else oeil_y - 18, ENCRE, 5))
    if larmes:
        m.append(goutte(oeil_x + 16, oeil_y + 30, 0.6, "#74c0fc"))
    if chapeau_:
        m.append(g([chemin(f"M {oeil_x - 70} {oeil_y - 26} Q {oeil_x - 10} {oeil_y - 120} {oeil_x + 50} {oeil_y - 26} Z", chapeau_),
                    trait(oeil_x - 70, oeil_y - 26, oeil_x + 50, oeil_y - 26, _assombrir(chapeau_, 0.7), 5),
                    cercle(oeil_x - 10, oeil_y - 60, 10, "#fa5252")]))
    return place(m, x, y, s, flip=flip)


def palmier(x, y, s=1.0, tronc="#c68642", feuilles="#2f9e44"):
    """Palmier ; (x, y) = pied du tronc."""
    m = [chemin("M -14 0 Q -30 -160 10 -300 L 32 -300 Q 4 -160 16 0 Z", tronc)]
    for k in range(6):
        m.append(trait(-20 + k * 2, -40 - k * 44, 28 - k * 2, -46 - k * 44, _assombrir(tronc, 0.8), 3))
    for ang in (-170, -135, -100, -70, -35, 0, 25, 155):
        a = math.radians(ang)
        cx, cy = 20 + math.cos(a) * 80, -300 + math.sin(a) * 50 + 20
        m.append(ellipse(cx, cy, 95, 22, feuilles if ang % 2 else _assombrir(feuilles, 0.85), rot=ang if abs(ang) < 90 else ang - 180))
    m += [cercle(10, -290, 12, "#8d5524"), cercle(32, -284, 12, "#8d5524")]
    return place(m, x, y, s)


def pyramide(x, y, s=1.0, couleur="#f4d58d", ombre="#e0b95b"):
    """Pyramide ; (x, y) = milieu de la base."""
    return place([poly([(-200, 0), (0, -210), (200, 0)], couleur), poly([(0, -210), (200, 0), (60, 0)], ombre)], x, y, s)


def nil(S, y=600, sable="#f4d58d", ciel_haut="#ffd8a8", ciel_bas="#fff4e6"):
    """Bords du Nil : ciel chaud, pyramides au loin, fleuve et berge de sable."""
    ciel(S, ciel_haut, ciel_bas)
    S.add(soleil(640, 150, 60, "#ffa94d", rayons=False))
    S.add(pyramide(170, y - 60, 0.7), pyramide(330, y - 60, 0.45))
    S.add(rect(0, y - 70, 800, 90, "#4dabf7"))
    S.add(chemin(" ".join(f"M {k * 110} {y - 40} q 25 -10 50 0" for k in range(8)), stroke="#a5d8ff", sw=5))
    S.add(rect(0, y + 10, 800, 800 - y, sable))
    S.add(chemin(f"M 0 {y + 14} Q 200 {y - 6} 400 {y + 14} T 800 {y + 14} L 800 {y + 30} L 0 {y + 30} Z", _assombrir(sable, 0.93)))


# ---------------------------------------------------------------------------
# Une souris verte
# ---------------------------------------------------------------------------

SOURIS_VERTE = dict(couleur="#8ce99a", visage="#ebfbee")


def souris_verte(x, y, s=1.0, **k):
    return perso("souris", x, y, s, **SOURIS_VERTE, **k)


def tiroir(x, y, s=1.0, couleur="#c68642", ouvert=True, dedans=""):
    """Commode à trois tiroirs, celui du haut ouvert ; (x, y) = milieu au sol."""
    m = [rect(-150, -300, 300, 290, couleur, rx=8), rect(-160, -312, 320, 20, _assombrir(couleur, 0.85), rx=6),
         rect(-140, -8, 20, 8, _assombrir(couleur, 0.7)), rect(120, -8, 20, 8, _assombrir(couleur, 0.7))]
    for k in range(3):
        yy = -280 + k * 90
        m += [rect(-130, yy, 260, 76, _assombrir(couleur, 0.92), rx=6), cercle(0, yy + 38, 8, "#ffd43b")]
    if ouvert:
        m += [poly([(-150, -280), (150, -280), (190, -240), (-190, -240)], "#343a40"),
              rect(-190, -240, 380, 80, _assombrir(couleur, 0.95), rx=6), cercle(0, -200, 9, "#ffd43b")]
        if dedans:
            m.append(dedans)
    return place(m, x, y, s)


def chapeau_haut(x, y, s=1.0, couleur="#343a40", ruban="#fa5252", rot=0):
    """Chapeau haut-de-forme ; (x, y) = milieu du bord."""
    m = [ellipse(0, 0, 90, 18, couleur), rect(-56, -120, 112, 120, couleur, rx=8),
         ellipse(0, -120, 56, 12, eclaircir(couleur, 0.3)), rect(-56, -34, 112, 20, ruban)]
    return place(m, x, y, s, rot=rot)


def poele(x, y, s=1.0, huile=True):
    """Poêle à frire ; (x, y) = centre."""
    m = [rect(90, -8, 150, 16, "#495057", rx=8), ellipse(0, 0, 110, 36, "#343a40"), ellipse(0, -4, 94, 26, "#f59f00" if huile else "#495057")]
    if huile:
        m += [cercle(-30, -6, 5, "#ffe066"), cercle(20, 2, 4, "#ffe066"), cercle(50, -8, 3, "#ffe066")]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Berceuses
# ---------------------------------------------------------------------------

def berceau(x, y, s=1.0, couleur="#fcc2d7", bois="#e8c39e", bebe=None, voile=False):
    """Berceau à bascule ; (x, y) = milieu au sol. `bebe` : dessin placé dedans."""
    m = []
    if voile:
        m.append(chemin("M -170 -150 Q -190 -330 -40 -360 Q 40 -370 30 -330 Q -110 -300 -120 -150 Z", "#fff0f6", opacity=0.95))
    m += [chemin("M -190 -10 Q 0 30 190 -10", stroke=bois, sw=14),
          rect(-160, -180, 320, 150, bois, rx=30), rect(-146, -168, 292, 50, "#fff", rx=20)]
    if bebe:
        m.append(bebe)
    m += [chemin("M -150 -130 L 150 -130 L 146 -60 Q 0 -40 -146 -60 Z", couleur),
          rect(-160, -60, 320, 40, bois, rx=14)]
    for k in range(4):
        m.append(coeur(-90 + k * 60, -96, 0.35, "#fff"))
    return place(m, x, y, s)


def bebe_dort(x, y, s=1.0, bonnet="#a5d8ff"):
    """Tête d'un bébé qui dort ; (x, y) = centre de la tête."""
    m = [cercle(0, 0, 46, "#fbd9bd"),
         chemin("M -48 -4 Q -50 -60 0 -62 Q 50 -60 48 -4 Q 20 -30 -48 -4 Z", bonnet),
         cercle(0, -64, 11, "#fff"),
         chemin("M -24 4 q 8 7 16 0", stroke=ENCRE, sw=3.5), chemin("M 8 4 q 8 7 16 0", stroke=ENCRE, sw=3.5),
         ellipse(-26, 20, 8, 5, ROSE, opacity=0.7), ellipse(26, 20, 8, 5, ROSE, opacity=0.7),
         ellipse(0, 24, 5, 3, "#e8590c", opacity=0.8)]
    return place(m, x, y, s)


def chambre_nuit(S, mur="#364fc7", plancher="#5c4a3a", papier="#4263eb", lune_=True):
    """Chambre plongée dans la pénombre, avec une fenêtre sur la nuit."""
    interieur(S, mur, plancher, 600, papier=papier, plinthe="#3b2f25")
    S.add(fenetre(520, 120, 180, 170, "#1c2a52", cadre="#dbe4ff", nuit_=lune_, rideaux="#9775fa"))
    S.add(tapis(400, 690, 260, 50, "#b197fc", "#9775fa"))


def ours_peluche(x, y, s=1.0, couleur="#d9a066"):
    """Petit ours en peluche assis ; (x, y) = sous les pattes."""
    m = [ellipse(-26, -8, 18, 12, _assombrir(couleur, 0.9)), ellipse(26, -8, 18, 12, _assombrir(couleur, 0.9)),
         ellipse(0, -40, 36, 34, couleur), ellipse(0, -34, 20, 18, eclaircir(couleur, 0.5)),
         cercle(-24, -104, 12, couleur), cercle(24, -104, 12, couleur), cercle(0, -86, 30, couleur),
         ellipse(0, -76, 12, 9, eclaircir(couleur, 0.5)), cercle(-10, -92, 3.5, ENCRE), cercle(10, -92, 3.5, ENCRE),
         ellipse(0, -80, 4, 3, ENCRE), ellipse(-34, -46, 10, 16, couleur, rot=20), ellipse(34, -46, 10, 16, couleur, rot=-20)]
    return place(m, x, y, s)


def poule_blanche(x, y, s=1.0, **k):
    """Poule blanche (pour « Dodo, l'enfant do »)."""
    from fables import coq
    k.setdefault("couleur", "#f8f9fa")
    k.setdefault("ventre", "#ffffff")
    return coq(x, y, s, poule=True, **k)


def grange(x, y, s=1.0, couleur="#c92a2a", ouverte=True):
    """Grange rouge ; (x, y) = milieu de la base."""
    m = [rect(-200, -220, 400, 220, couleur), poly([(-220, -210), (0, -340), (220, -210)], _assombrir(couleur, 0.8)),
         rect(-80, -170, 160, 170, "#5c3a1e" if ouverte else "#fff4e6")]
    if not ouverte:
        m += [trait(-80, -170, 80, 0, couleur, 10), trait(80, -170, -80, 0, couleur, 10)]
    else:
        m += [rect(-70, -40, 140, 40, "#f6c453"), chemin("M -70 -40 Q 0 -90 70 -40 Z", "#f6c453")]
    m.append(chemin("M -30 -270 Q 0 -300 30 -270 L 30 -240 L -30 -240 Z", "#fff4e6"))
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Il était un petit navire
# ---------------------------------------------------------------------------

def navire(x, y, s=1.0, coque="#c92a2a", voile="#fff9db", drapeau="#4dabf7", penche=0, marins=()):
    """Petit voilier de profil, proue à droite ; (x, y) = milieu sur la ligne d'eau.
    `marins` : dessins (coordonnées locales) placés sur le pont, avant la coque."""
    m = [trait(0, -40, 0, -400, "#8d5524", 10),
         chemin("M 10 -390 Q 150 -260 170 -60 L 10 -60 Z", voile, stroke=_assombrir(voile, 0.85), sw=4),
         chemin("M -10 -350 Q -120 -220 -170 -60 L -10 -60 Z", voile, stroke=_assombrir(voile, 0.85), sw=4),
         poly([(0, -400), (70, -385), (0, -370)], drapeau)]
    m += list(marins)
    m += [chemin("M -240 -60 L 250 -60 Q 230 30 150 40 L -160 40 Q -230 20 -240 -60 Z", coque),
          rect(-236, -70, 484, 18, _assombrir(coque, 0.75), rx=6)]
    for k in range(5):
        m.append(cercle(-150 + k * 70, -10, 12, "#fff4e6", stroke=_assombrir(coque, 0.7), stroke_width=4))
    return place(m, x, y, s, rot=penche)


def mer(S, y=520, haut="#74c0fc", bas="#e7f5ff", eau_c="#1c7ed6", eau_c2="#4dabf7", graine=1):
    ciel(S, haut, bas)
    S.add(nuage(160, 140, 0.8, opacity=0.9), nuage(620, 90, 0.6, opacity=0.9))
    S.add(el("rect", x=0, y=y, width=800, height=800 - y, fill=eau_c))
    for k in range(7):
        yy = y + 24 + k * 44
        x0 = (k % 2) * 50 - 30
        S.add(chemin(" ".join(f"M {x0 + i * 100} {yy} q 25 -14 50 0" for i in range(9)), stroke=eau_c2, sw=6))


def vagues_devant(y, couleur="#1c7ed6", couleur2="#4dabf7"):
    """Bande de vagues à mettre devant la coque d'un bateau."""
    d = f"M 0 {y} " + " ".join(f"q 25 -18 50 0" for _ in range(16)) + f" L 800 800 L 0 800 Z"
    return g([chemin(d, couleur), chemin(" ".join(f"M {-25 + i * 100} {y + 34} q 25 -12 50 0" for i in range(9)), stroke=couleur2, sw=5)])


def mousse(x, y, s=1.0, **k):
    """Le petit mousse : marinière rayée et bonnet à pompon."""
    k.setdefault("coiffure", "courts")
    k.setdefault("cheveux", "blond")
    return personne(x, y, s, habit="#f8f9fa", robe=False, jambes="#1c7ed6", **k) + place(
        [rect(-44, -96 + j * 16, 88, 7, "#1c7ed6") for j in range(4)]
        + [chemin("M -52 -196 Q 0 -240 52 -196 Z", "#1c7ed6"), cercle(0, -228, 12, "#fa5252")], x, y, s)


def paille(x, y, s=1.0, longue=True, rot=0):
    """Brin de paille à tirer."""
    h = 110 if longue else 50
    return place([rect(-5, -h, 10, h, "#f6c453", rx=4), trait(0, -h + 6, 0, -6, "#e0a800", 2)], x, y, s, rot=rot)


# ---------------------------------------------------------------------------
# Sur le pont d'Avignon
# ---------------------------------------------------------------------------

def pont_avignon(x, y, s=1.0, pierre="#e9d8b4", ombre="#cbb58a", arches=4):
    """Le pont Saint-Bénezet, avec ses arches, interrompu au milieu du fleuve,
    et sa petite chapelle ; (x, y) = bout gauche du tablier."""
    m = []
    w = 170
    L = arches * w
    m.append(rect(0, -30, L, 40, pierre))
    m.append(rect(0, -44, L, 16, ombre))
    for k in range(arches):
        ax = k * w
        m.append(rect(ax + 10, 0, w - 20, 170, pierre))
        m.append(chemin(f"M {ax + 30} 170 L {ax + 30} 80 Q {ax + w / 2} 10 {ax + w - 30} 80 L {ax + w - 30} 170 Z", "#1c7ed6"))
        m.append(poly([(ax - 14, 170), (ax - 14, 60), (ax + 10, 40), (ax + 34, 60), (ax + 34, 170)], ombre))
    # bout cassé
    m.append(poly([(L - 10, -44), (L + 20, -30), (L + 5, -10), (L + 25, 10), (L - 10, 170), (L - 10, -44)], pierre))
    # chapelle
    m += [rect(170, -150, 110, 110, pierre), poly([(160, -146), (225, -210), (290, -146)], "#e8590c"),
          chemin("M 210 -40 L 210 -90 Q 225 -110 240 -90 L 240 -40 Z", "#8d5524"),
          rect(214, -250, 24, 50, pierre), poly([(208, -246), (226, -276), (244, -246)], "#e8590c")]
    return place(m, x, y, s)


def rhone(S, y=520, ciel_haut="#a5d8ff", ciel_bas="#fff9db"):
    """Le Rhône, Avignon et le palais des Papes au loin."""
    ciel(S, ciel_haut, ciel_bas)
    S.add(soleil(680, 110, 48))
    # remparts et palais au loin
    S.add(rect(0, y - 110, 360, 110, "#f1e3c8"))
    for k in range(10):
        S.add(rect(k * 36, y - 126, 22, 18, "#f1e3c8"))
    S.add(rect(60, y - 220, 170, 110, "#f1e3c8"), rect(80, y - 260, 50, 150, "#e9d8b4"), rect(180, y - 250, 40, 140, "#e9d8b4"))
    S.add(rect(0, y, 800, 800 - y, "#1c7ed6"))
    for k in range(6):
        S.add(chemin(" ".join(f"M {(k % 2) * 60 + i * 130} {y + 40 + k * 46} q 25 -12 50 0" for i in range(7)), stroke="#4dabf7", sw=5))


def danseur(x, y, s=1.0, dame=False, **k):
    """Beau monsieur (chapeau et redingote) ou belle dame (robe longue et coiffe)."""
    chap = k.pop("chapeau_", True)
    if dame:
        k.setdefault("coiffure", "chignon")
        k.setdefault("habit", "#f783ac")
        return personne(x, y, s, robe=True, **k)
    k.setdefault("coiffure", "courts")
    k.setdefault("habit", "#364fc7")
    k.setdefault("jambes", "#212529")
    haut = personne(x, y, s, robe=False, acc=("col",) + tuple(k.pop("acc", ())), **k)
    if chap:
        haut += place([ellipse(0, -198, 66, 12, "#212529"), rect(-40, -290, 80, 94, "#212529", rx=6), rect(-40, -224, 80, 14, "#fa5252")], x, y, s)
    return haut


def trompette(x, y, s=1.0, rot=0):
    """Trompette ; (x, y) = embouchure, pavillon à droite."""
    m = [rect(0, -6, 130, 12, OR, rx=5), poly([(120, -8), (180, -34), (180, 34), (120, 8)], OR),
         ellipse(180, 0, 8, 34, "#e67700"), rect(40, -26, 12, 22, OR), rect(62, -26, 12, 22, OR), rect(84, -26, 12, 22, OR)]
    return place(m, x, y, s, rot=rot)


def tambour_objet(x, y, s=1.0, couleur="#fa5252"):
    """Tambour ; (x, y) = centre du dessus."""
    m = [rect(-60, 0, 120, 90, couleur, rx=6), ellipse(0, 90, 60, 14, couleur), ellipse(0, 0, 60, 14, "#fff4e6", stroke="#c92a2a", stroke_width=3),
         chemin("M -60 10 L -30 80 L 0 10 L 30 80 L 60 10", stroke="#ffd43b", sw=5)]
    return place(m, x, y, s)


# ---------------------------------------------------------------------------
# Promenons-nous dans les bois
# ---------------------------------------------------------------------------

def arbre_loup(x, y, s=1.0):
    """Gros arbre au tronc large, derrière lequel on peut se cacher ; (x, y) = pied."""
    m = [chemin("M -70 0 Q -50 -120 -60 -300 L 60 -300 Q 50 -120 70 0 Z", "#8d5524"),
         cercle(-110, -360, 110, "#2f9e44"), cercle(90, -370, 120, "#2f9e44"), cercle(0, -450, 120, "#37b24d"),
         ellipse(0, -240, 18, 26, "#5c3a1e")]
    return place(m, x, y, s)


def buisson_cache(x, y, s=1.0, yeux_=False):
    """Buisson touffu ; avec `yeux_`, deux yeux brillent dedans."""
    m = [cercle(-70, -50, 60, "#2b8a3e"), cercle(0, -80, 75, "#2f9e44"), cercle(70, -50, 60, "#2b8a3e"), rect(-130, -50, 260, 50, "#2f9e44", rx=10)]
    if yeux_:
        m += [ellipse(-22, -70, 14, 10, "#ffe066"), ellipse(22, -70, 14, 10, "#ffe066"), cercle(-20, -70, 5, ENCRE), cercle(24, -70, 5, ENCRE)]
    return place(m, x, y, s)


def vetement(x, y, s=1.0, sorte="chemise", couleur="#4dabf7", rot=0):
    """Vêtement suspendu : chemise, culotte, chaussettes, bottes."""
    if sorte == "chemise":
        m = [poly([(-60, -90), (-100, -60), (-80, -30), (-50, -50), (-50, 40), (50, 40), (50, -50), (80, -30), (100, -60), (60, -90)], couleur),
             poly([(-20, -90), (0, -60), (20, -90)], "#fff")] + [cercle(0, -40 + k * 24, 4, "#fff") for k in range(3)]
    elif sorte == "culotte":
        m = [poly([(-60, -40), (60, -40), (70, 50), (10, 50), (0, 0), (-10, 50), (-70, 50)], couleur), rect(-60, -40, 120, 14, _assombrir(couleur, 0.8))]
    elif sorte == "chaussettes":
        m = [chemin(f"M {dx - 20} -60 L {dx + 10} -60 L {dx + 10} 20 Q {dx + 50} 20 {dx + 50} 40 L {dx - 20} 40 Z", couleur) for dx in (-40, 30)]
        m += [rect(dx - 20, -60, 30, 12, "#fff") for dx in (-40, 30)]
    else:  # bottes
        m = [chemin(f"M {dx - 24} -70 L {dx + 14} -70 L {dx + 14} 14 Q {dx + 56} 14 {dx + 56} 40 L {dx - 24} 40 Z", couleur) for dx in (-50, 30)]
    return place(m, x, y, s, rot=rot)


# ---------------------------------------------------------------------------
# Ainsi font, font, font
# ---------------------------------------------------------------------------

def marionnette(x, y, s=1.0, habit="#fa5252", bras="haut", expr="rire", fils=True, rot=0, **k):
    """Marionnette à fils : un personnage suspendu à une croix de bois.
    (x, y) = sous les pieds (qui ne touchent pas le sol)."""
    m = []
    if fils:
        m += [rect(-90, -420, 180, 14, "#a0522d", rx=6), rect(-7, -460, 14, 90, "#a0522d", rx=6)]
        mg, md = POSES_MAINS[bras] if bras in POSES_MAINS else ((-52, -40), (52, -40))
        for px, py in (mg, md, (-30, -196), (30, -196)):
            m.append(trait(px * 1.3 if abs(px) > 40 else px, -410, px, py, "#868e96", 1.6))
    k.setdefault("coiffure", "boucles")
    k.setdefault("cheveux", "roux")
    m.append(personne(0, 0, 1.0, habit=habit, robe=False, jambes=_assombrir(habit, 0.7), bras=bras, expr=expr,
                      acc=("col",), **k))
    return place(m, x, y, s, rot=rot)


from base import POSES as POSES_MAINS  # noqa: E402


def theatre(S, rideau="#c92a2a", fond_="#fff3bf"):
    """Petit théâtre de marionnettes : scène, rideaux et fronton."""
    S.add(rect(0, 0, 800, 800, "#5f3dc4"))
    S.add(rect(80, 140, 640, 520, fond_))
    for k in range(8):
        S.add(rect(80 + k * 80, 140, 40, 520, "#ffe066", opacity=0.3))
    S.add(rect(40, 640, 720, 160, "#8d5524"), rect(40, 640, 720, 20, "#a0693a"))
    S.add(chemin("M 60 100 L 220 100 Q 160 380 200 680 L 60 680 Z", rideau))
    S.add(chemin("M 740 100 L 580 100 Q 640 380 600 680 L 740 680 Z", rideau))
    S.add(chemin("M 40 60 L 760 60 L 760 150 Q 700 190 640 150 Q 580 190 520 150 Q 460 190 400 150 Q 340 190 280 150 Q 220 190 160 150 Q 100 190 40 150 Z", _assombrir(rideau, 0.85)))
    S.add(rect(30, 40, 740, 30, OR, rx=8))


# ---------------------------------------------------------------------------
# Meunier, tu dors
# ---------------------------------------------------------------------------

def moulin_vent(x, y, s=1.0, rot=0, vitesse=False, mur="#f1e3c8", toit="#c92a2a", ailes_c="#fff9db"):
    """Grand moulin à vent ; (x, y) = milieu de la base ; `rot` fait tourner les ailes."""
    m = [poly([(-110, 0), (-80, -300), (80, -300), (110, 0)], mur),
         poly([(-100, -296), (0, -390), (100, -296)], toit),
         chemin("M -34 0 L -34 -70 Q 0 -100 34 -70 L 34 0 Z", "#8d5524"),
         rect(-24, -210, 48, 48, "#a5d8ff", stroke="#fff", stroke_width=5)]
    ailes = []
    for k in range(4):
        a = rot + k * 90
        ailes.append(g([rect(-8, -250, 16, 250, "#8d5524"), rect(8, -240, 60, 200, ailes_c, stroke="#c68642", stroke_width=4)]
                       + [trait(8, -240 + j * 40, 68, -240 + j * 40, "#c68642", 3) for j in range(1, 5)],
                       transform=f"rotate({n(a)})"))
    m.append(g(ailes, transform="translate(0 -320)"))
    if vitesse:
        for k in range(3):
            r = 270 + k * 22
            a0, a1 = math.radians(rot - 20 - k * 8), math.radians(rot + 40 - k * 8)
            m.append(chemin(f"M {n(math.cos(a0) * r)} {n(-320 + math.sin(a0) * r)} A {r} {r} 0 0 1 {n(math.cos(a1) * r)} {n(-320 + math.sin(a1) * r)}",
                            stroke=ENCRE, sw=5, opacity=0.5))
    m.append(cercle(0, -320, 18, "#495057"))
    return place(m, x, y, s)


def meunier(x, y, s=1.0, **k):
    """Le meunier : tablier et bonnet blancs de farine."""
    k.setdefault("coiffure", "courts")
    k.setdefault("cheveux", "gris")
    k.setdefault("barbe", "#ced4da")
    return personne(x, y, s, habit="#e9ecef", robe=False, jambes="#868e96", acc=("bonnet_nuit",) + tuple(k.pop("acc", ())),
                    couleur_acc="#fff", **k)


def sac_farine(x, y, s=1.0):
    """Sac de farine ; (x, y) = milieu du fond."""
    m = [chemin("M -50 0 Q -64 -80 -36 -120 L 36 -120 Q 64 -80 50 0 Z", "#f1e3c8"),
         chemin("M -36 -120 Q 0 -140 36 -120 L 26 -140 L -26 -140 Z", "#e9d8b4"),
         texte(0, -46, "FARINE", 22, "#a0693a")]
    return place(m, x, y, s)
