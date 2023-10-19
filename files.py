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

    print(file_path)

    filename = os.path.basename(file_path)
    root.title("{} - JSON-Edit".format(filename))

    read_data(file_path)

    onopenfunc()
    update_save_path(file_path)


def update_save_path(new_save_path):
    save_path = new_save_path
    return save_path


def get_file_path():
    print(file_path)
    return file_path


def save_as_file(tableaux, root):
    "Enregistrer le fichier au format JSON"
    save_path = filedialog.asksaveasfilename(
        title="Enregistrer au format JSON", defaultextension=".json", filetypes=[("Fichier JSON", "*.json")])

    data = []

    for tableau in tableaux:
        # Pour chaque entrée du tableau
        for i in range(0, len(tableau.boutons_entrees), 2):
            key = tableau.boutons_entrees[i].get()
            value = tableau.boutons_entrees[i+1].get()
            data.append({key: value})

    with open(save_path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=True)

    root.title(os.path.basename(save_path))
