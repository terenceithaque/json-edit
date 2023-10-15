# Gérer les fichiers JSON
from tkinter import filedialog
import json
import os
from donnees import read_data


save_path = ""


def open_json(root, onopenfunc):
    "Ouvrir un fichier JSON"
    global file_path
    file_path = filedialog.askopenfilename(
        title="Ouvrir un fichier JSON", filetypes=[("Fichiers JSON", "*.json")])

    filename = os.path.basename(file_path)
    root.title("{} - JSON-Edit".format(filename))

    read_data(file_path)

    onopenfunc()


def update_save_path(new_save_path):
    save_path = new_save_path
    return save_path


def get_file_path():
    return file_path


def save_as_file(tableau):
    "Sauvegarder sous un fichier JSON"
    save_path = filedialog.asksaveasfilename(
        title="Enregistrer dans un fichier JSON", defaultextension=".json", filetypes=["Fichier JSON", "*.json"])

    for entree in tableau:
        str_entree = entree.get()
        with open(save_as_file, "w") as wf:
            wf.write(str_entree)
            wf.close()

    return update_save_path(save_path)
