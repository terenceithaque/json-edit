# Gérer les fichiers JSON
from tkinter import filedialog
import json
import os
from donnees import read_data
from tableau import *

liste_tableaux = []


def open_json(root):
    "Ouvrir un fichier JSON"
    global file_path
    file_path = filedialog.askopenfilename(
        title="Ouvrir un fichier JSON", filetypes=[("Fichiers JSON", "*.json")])

    filename = os.path.basename(file_path)
    root.title("{} - JSON-Edit".format(filename))

    read_data(file_path)

    tableau = Tableau(file_path, root)
    liste_tableaux.append(tableau)
    print("Premier tableau", liste_tableaux[0])

    if len(liste_tableaux) > 1:
        liste_tableaux[0].destroy()
        del liste_tableaux[0]
        print("Premier tableau suprimmé !")
