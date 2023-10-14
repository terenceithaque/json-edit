# Gérer les fichiers JSON
from tkinter import filedialog
import json
import os
from donnees import read_data
from tableau import *


def open_json(root):
    "Ouvrir un fichier JSON"
    global file_path
    file_path = filedialog.askopenfilename(
        title="Ouvrir un fichier JSON", filetypes=[("Fichiers JSON", "*.json")])

    filename = os.path.basename(file_path)
    root.title("{} - JSON-Edit".format(filename))

    tableau = Tableau(file_path, root)

    read_data(file_path)
