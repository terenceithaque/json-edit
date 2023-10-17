# Tableau
from tkinter import *
import json
from donnees import read_data
from tkinter import simpledialog
from tkinter import filedialog


class Tableau:
    "Tableau pour représenter les entrées des fichiers JSON"

    def __init__(self, path, root):
        if path is not None:
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

        else:
            self.boutons_entrees = []
            self.entrees = []
            entree_cle = Entry(root)
            entree_cle.pack(fill="x")
            self.boutons_entrees.append(entree_cle)
            entree_valeur = Entry(root)
            entree_valeur.pack(fill="x")
            self.boutons_entrees.append(entree_valeur)
            self.entrees.append((entree_cle, entree_valeur))

        root.bind("<Control-f>", self.search)
        root.bind("<Control-c>", lambda: self.copier(root.focus_get()))
        root.bind("<Control-s>", self.save_as_file)
        root.bind("<Control-e>", lambda event: self.ajouter_entree(root, event))

    def search(self, event):
        "Rechercher un élément du fichier JSON"

        recherche = simpledialog.askstring(
            "Element à rechercher", "Entrez l'élément à rechecher dans le tableau (tout élément correspondant verra sa colonne mise en jaune) :")

        # Rechercher le texte dans les entrées
        for entree in self.boutons_entrees:
            if recherche in entree.get():
                # Si le texte est trouvé, mettre en évidence l'entrée
                entree.config(bg="yellow")
                entree.config(bg="yellow")

            else:
                entree.config(bg="white")

    def destroy(self):
        for bouton in self.boutons_entrees:
            bouton.destroy()

    def save_as_file(self, event):
        "Sauvegarder sous un fichier JSON"
        save_path = filedialog.asksaveasfilename(
            defaultextension=".json", title="Enregistrer sous un fichier JSON", filetypes=[("JSON", "*.json")])
        for bouton_entree in self.boutons_entrees:
            print(bouton_entree)
            str_entree = bouton_entree.get()
            with open(save_path, "w") as wf:
                json.dump(str_entree, wf)

    def ajouter_entree(self, root, event):
        "Ajouter un widget Entrée au tableau"
        nouvelle_entree = Entry(root)
        nouvelle_entree.pack(fill="x")
        self.boutons_entrees.append(nouvelle_entree)

    def remplacer(self):
        "Remplacer élément du tableau par un autre"
        original_str = simpledialog.askstring(
            "Entrez l'élément à remplacer", "Saisissez l'élément à remplacer dans toutes les entrées :")
        new_str = simpledialog.askstring(
            "Entrez le nouvel élément", "Saisissez le nouvel élément :")
        for entree in self.boutons_entrees:  # Pour chaque entrée du tableau
            if original_str in entree.get():
                entree.delete(
                    len(entree.get()) - len(original_str), len(original_str))
                entree.insert(len(original_str), new_str)
