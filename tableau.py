# Tableau
from tkinter import *
import json
from donnees import read_data
from tkinter import simpledialog


class Tableau:
    "Tableau pour représenter les entrées des fichiers JSON"

    def __init__(self, path, root):
        donnees = read_data(path)
        self.n_lignes = len(donnees)  # Nombre de lignes
        self.boutons_entrees = []
        self.entrees = []
        for cle in donnees:
            texteEntree1 = StringVar()  # Texte de la première entrée de chaque ligne
            texteEntree1.set(str(cle))
            texteEntree2 = StringVar()  # Texte de la deuxième entrée de chaque ligne
            texteEntree2.set(str(donnees[cle]))
            entree_cle = Entry(root, textvariable=texteEntree1)
            entree_cle.pack(fill="x")
            self.boutons_entrees.append(entree_cle)
            entree_valeur = Entry(root, textvariable=texteEntree2)
            entree_valeur.pack(fill="x")
            self.boutons_entrees.append(entree_valeur)
            self.entrees.append((entree_cle, entree_valeur))

        root.bind("<Control-f>", self.search)

    def search(self, event):
        "Rechercher un élément du fichier JSON"

        recherche = simpledialog.askstring(
            "Element à rechercher", "Entrez l'élément à rechecher dans le tableau :")

        # Rechercher le texte dans les entrées
        for entree_cle, entree_valeur in self.entrees:
            if recherche in entree_cle.get() or recherche in entree_valeur.get():
                # Si le texte est trouvé, mettre en évidence l'entrée
                entree_cle.config(bg="yellow")
                entree_valeur.config(bg="yellow")

            else:
                entree_cle.config(bg="white")
                entree_valeur.config(bg="white")

    def destroy(self):
        for bouton in self.boutons_entrees:
            bouton.destroy()
