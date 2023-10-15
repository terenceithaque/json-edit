# Programme pour visualiser et éditer graphqiuement des fichiers JSON
from tkinter import *  # Importer tkinter pour l'interface graphique
import json  # Importer le module JSON
from files import *
from donnees import read_data
from tableau import *


class Application(Tk):
    "Application"

    def __init__(self):
        super().__init__()  # Appeler le constructeur
        self.title("JSON-Edit")
        self.barre_menu = Menu(self, tearoff=0)  # Créer une barre de menus
        # Créer un menu "Fichier"
        self.menu_fichier = Menu(self.barre_menu, tearoff=0)
        self.menu_fichier.add_command(
            label="Ouvrir un fichier JSON", command=lambda: open_json(self, self.creer_tableau))
        self.barre_menu.add_cascade(label="Fichier", menu=self.menu_fichier)
        # Créer un menu "Edition"
        self.menu_edition = Menu(self.barre_menu, tearoff=0)
        self.menu_edition.add_command(
            label="Afficher les commandes & raccourcis claviers", command=self.afficher_raccourcis)

        self.barre_menu.add_cascade(label="Edition", menu=self.menu_edition)
        self.config(menu=self.barre_menu)

        self.liste_tableaux = []

    def creer_tableau(self):
        "Créer un tableau"
        tableau = Tableau(get_file_path(), self)

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


app = Application()  # Créer une instance de l'application
app.mainloop()
