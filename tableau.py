# Tableau
from tkinter import *
import json
from donnees import read_data


class Tableau:
    "Tableau pour représenter les entrées des fichiers JSON"

    def __init__(self, path, root):
        donnees = read_data(path)
        texteEntree1 = StringVar()  # Texte de la première entrée de chaque ligne
        texteEntree2 = StringVar()  # Texte de la deuxième entrée de chaque ligne
        self.n_lignes = len(donnees)  # Nombre de lignes
        n = 0  # Nombre actuel de lignes du tableau
        while n < self.n_lignes:
            for cle in donnees:
                texteEntree1.set(str(cle))
                texteEntree2.set(str(donnees[cle]))
                entree_cle = Entry(root, textvariable=texteEntree1)
                entree_cle.pack()
                entree_valeur = Entry(root, textvariable=texteEntree2)
                entree_valeur.pack()

            n += 1
