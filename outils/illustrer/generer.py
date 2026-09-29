"""
Génère les illustrations SVG des chansons (et du recueil).

    python3 outils/illustrer/generer.py              # toutes les chansons
    python3 outils/illustrer/generer.py frere-jacques  # une seule chanson

Chaque chanson est décrite dans `histoires/<id_avec_soulignés>.py` : une
variable ID et une liste IMAGES de couples (nom de fichier, fonction qui
renvoie une Scene). Les images sont écrites dans `chansons/<id>/images/`.
"""
import importlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)

import base  # noqa: E402


def modules():
    for nom in sorted(os.listdir(os.path.join(ICI, "histoires"))):
        if nom.endswith(".py") and not nom.startswith("_"):
            yield importlib.import_module(f"histoires.{nom[:-3]}")


def generer(module):
    # numérotation des identifiants SVG propre à chaque chanson : le résultat ne
    # dépend pas des autres chansons générées en même temps
    base._compteur[0] = 0
    dossier = os.path.join(RACINE, "chansons", module.ID, "images")
    for nom, fabrique in module.IMAGES:
        fabrique().enregistrer(os.path.join(dossier, nom))
    print(f"{module.ID} : {len(module.IMAGES)} images")


if __name__ == "__main__":
    voulus = set(sys.argv[1:])
    for m in modules():
        if not voulus or m.ID in voulus:
            generer(m)
