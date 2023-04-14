import tkinter as tk
from dataToDB.creationBD import creationBD
from dataToDB.insertionBD import toutInserer
from graphics.FenetreGraphiquePrincipale import FenetreGraphique


class ChargerBase(FenetreGraphique):
    def __init__(self):
        super().__init__()
        print(self.BASETEST.get())

    def executeUpdateBase(self):
        '''
        TESTER, CREER, INSERER, REQUETER en fonction des var 1, 2, 4 et 4
        '''
        self.root.update() # Met à jour l'état des cases à cocher

        if self.BASETEST.get():
            #on cré la base de données test ou non
            creationBD(True)
            toutInserer(True)
            self.BASETEST.set(False)

        if self.BASEREELLE:
            #on cré la base de données test ou non
            creationBD(False)
            toutInserer(False)
            self.BASEREELLE.set(False)

    
    def miseAJourBase(self):
        '''
        demander avec des bouton si oui ou non le user veut : TESTER, CREER, INSERER, REQUETER
        '''
        #créer un cadre pour entourer le tout
        memeX = (10*self.width)/400
        cadre = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        cadre.place(x=memeX, y=10)
        cadre.config(width=(90*self.width)/400, height=100)

        checkbutton1 = tk.Checkbutton(cadre, text="BD de test", variable=self.BASETEST)
        checkbutton1.place(x=memeX,y=10)

        checkbutton1 = tk.Checkbutton(cadre, text="BD réelle", variable=self.BASEREELLE)
        checkbutton1.place(x=memeX,y=30)

        bouton = tk.Button(cadre, text="Charger", command=self.executeUpdateBase, state="normal")
        bouton.place(x=(21*self.width)/400, y=64)