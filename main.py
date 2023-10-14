# Programme pour visualiser et éditer graphqiuement des fichiers JSON
from tkinter import *  # Importer tkinter pour l'interface graphique
import json  # Importer le module JSON
from files import *
from donnees import read_data


class Application(Tk):
    "Application"

    def __init__(self):
        super().__init__()  # Appeler le constructeur
        self.title("JSON-Edit")
        self.barre_menu = Menu(self, tearoff=0)  # Créer une barre de menus
        # Créer un menu "Fichier"
        self.menu_fichier = Menu(self.barre_menu, tearoff=0)
        self.menu_fichier.add_command(
            label="Ouvrir un fichier JSON", command=lambda: open_json(self))
        self.barre_menu.add_cascade(label="Fichier", menu=self.menu_fichier)
        self.config(menu=self.barre_menu)


app = Application()  # Créer une instance de l'application
app.mainloop()
