# Programme pour visualiser et éditer graphqiuement des fichiers JSON
from tableau import *
from donnees import read_data
from tkinter import *  # Importer tkinter pour l'interface graphique
import json  # Importer le module JSON
from files import *


class Application(Tk):
    "Application"

    def __init__(self):
        super().__init__()  # Appeler le constructeur
        self.title("JSON-Edit")
        self.barre_menu = Menu(self, tearoff=0)  # Créer une barre de menus
        # Créer un menu "Fichier"
        self.menu_fichier = Menu(self.barre_menu, tearoff=0)
        self.menu_fichier.add_command(
            label="Nouveau fichier JSON", command=lambda: self.creer_tableau(set_path=None))
        self.menu_fichier.add_command(
            label="Ouvrir un fichier JSON", command=lambda: open_json(self, lambda: self.creer_tableau(True)))
        self.barre_menu.add_cascade(label="Fichier", menu=self.menu_fichier)
        # Créer un menu "Edition"
        self.menu_edition = Menu(self.barre_menu, tearoff=0)
        self.menu_edition.add_command(
            label="Afficher les commandes & raccourcis claviers", command=self.afficher_raccourcis)
        self.menu_edition.add_command(
            label="Remplacer dans les entrées", command=self.replace)

        self.barre_menu.add_cascade(label="Edition", menu=self.menu_edition)

        # Créer un menu "Insertion"
        self.menu_insertion = Menu(self.barre_menu, tearoff=0)
        self.menu_insertion.add_command(
            label="Insérer une nouvelle entrée Ctrl + E", command=lambda: self.add_entry(None))
        self.barre_menu.add_cascade(
            label="Insertion", menu=self.menu_insertion)
        self.config(menu=self.barre_menu)

        self.liste_tableaux = []

    def creer_tableau(self, set_path):
        "Créer un tableau"
        if set_path is not None:
            tableau = Tableau(get_file_path(), self)

        else:
            tableau = Tableau(None, self)

        self.liste_tableaux.append(tableau)
        print("Longueur de la liste :", len(self.liste_tableaux))
        print("Premier tableau", self.liste_tableaux[0])

        if len(self.liste_tableaux) > 1:
            self.liste_tableaux[0].destroy()
            del self.liste_tableaux[0]
            print("Premier tableau suprimmé !")

    def afficher_raccourcis(self):
        "Afficher les raccourcis clavier"
        fen_raccourcis = Toplevel()
        fen_raccourcis.title("Commandes & raccourcis clavier")
        label_copier = Label(fen_raccourcis, text="Copier : Ctrl + C")
        label_copier.pack()
        label_coller = Label(fen_raccourcis, text="Coller : Ctrl + V")
        label_coller.pack()
        label_rechercher = Label(
            fen_raccourcis, text="Rechercher dans le tableau : Ctrl + F")
        label_rechercher.pack()

    def add_entry(self, event):
        "Ajouter une entrée à un tableau existant"
        for tableau in self.liste_tableaux:
            tableau.ajouter_entree(self, event)

    def replace(self):
        for tableau in self.liste_tableaux:
            tableau.remplacer()


app = Application()  # Créer une instance de l'application
app.mainloop()
