import tkinter as tk
from graphics.erreurs import dicoErreur
from dataToDB.creationBD import creationBD
from dataToDB.insertionBD import toutInserer
from dataToDB.query import query

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import os


WORD_CONVERTOR = {
    "Moyenne" : "AVG",
    "Somme" : "SUM",
    "Maximum" : "MAX",
    "Minimum" : "MIN",
    "Années" : "annees",
    "Région" : "reg",
    "Département" : "dept"
}


class FenetreGraphique:
    def __init__(self, x=500, y=300):
        self.root = tk.Tk()
        #taille fenetre
        self.width = x
        self.height = y

        self.BASETEST = tk.BooleanVar()
        self.BASEREELLE = tk.BooleanVar()
        self.baseTestExists = os.path.exists("projetPopulationTEST.db")
        self.baseReelleExists = os.path.exists("projetPopulation.db")

        self.requete = tk.Text(self.root, width=self.convX(35), height=(5*self.height)//400 + 1)
        self.boutonsBaseSelect = tk.StringVar()
        self.boutonsBaseSelect.set("None")
        self.errorText = None


        self.afficheTab = tk.BooleanVar()
        self.afficheTab.set(False)
        self.fig = None


    def convX(self, x):
        # converti les x en une bonne longeur
        return (x*self.width)//400


    def lancerFenetre(self):
        ''''
        lance la fenetre au centre de l'écran
        '''
        # Obtenir la taille de l'écran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()

        # Calculer les coordonnées x et y pour placer la fenêtre au centre de l'écran
        x = (largeur_ecran // 2) - (self.width // 2)
        y = (hauteur_ecran // 2) - (self.height // 2)

        # le user ne peut pas la redimentionner
        self.root.resizable(False, False)

        # lancer la fenetre en fonction de la taille de l'écran
        self.root.geometry("500x300+{}+{}".format(x, y))
    

    '''
    def faireDemande(self):
        # Créer le premier champ de texte et lui lier l'événement <Return>
        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()
        self.entry1.bind("<Return>", self.traiter_entree1)
        
        # Créer le deuxième champ de texte et lui lier l'événement <Return>
        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()
        self.entry2.bind("<Return>", self.traiter_entree2)
    
    def traiter_entree1(self, event):
        texte = self.entry1.get()
        print("Texte saisi dans le premier champ :", texte)
        self.entry2.focus_set()
    '''


    ########################################################################################################

    def continuerAfficher(self):
        self.root.mainloop()


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

        if self.BASEREELLE.get():
            #on cré la base de données test ou non
            creationBD(False)
            toutInserer(False)
            self.BASEREELLE.set(False)





    ########################################################################################################
    '''
    PARTIE LA MISE A JOUR / CREATION DES BASES DE DONNEES
    '''

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





    ########################################################################################################
    '''
    PARTIE SUR LES REQUETES QUE L'ON DEMANDE A UNE CERTAINE BD
    '''

    def requeterBase(self):
        boutonExec = tk.Button(self.root, text="Exécuter", command=self.traiterRequete, state="normal")
        boutonExec.place(x=(110*self.width)/400, y=10)

        texteRequete = tk.Label(self.root, text="la requête avec BD")
        texteRequete.place(x=(160*self.width)/400, y=13)

        self.boutonsChoixBase()

        self.requete.place(x=(110*self.width)/400, y=42)


    def boutonsChoixBase(self):
        '''
        si on clique sur le bouton test alors on déchoche l'autre et inverssement
        '''
        self.boutonSelecBaseTest = tk.Radiobutton(self.root, text="de test", variable=self.boutonsBaseSelect, value="baseTest", command=self.checkChoixbase)
        self.boutonSelecBaseTest.place(x=(242*self.width)/400,y=11)

        texteOu = tk.Label(self.root, text="ou")
        texteOu.place(x=(290*self.width)/400, y=13)

        self.boutonSelectBaseReelle = tk.Radiobutton(self.root, text="réelle", variable=self.boutonsBaseSelect, value="baseReelle",command=self.checkChoixbase)
        self.boutonSelectBaseReelle.place(x=(308*self.width)/400,y=11)


    def checkChoixbase(self):
        '''
        si l'un est vrai on met l'autre en faux
        '''
        if self.boutonsBaseSelect.get() == "None":
            self.boutonSelectBaseReelle.deselect()
            self.boutonSelecBaseTest.deselect()
        elif self.boutonsBaseSelect.get() == "baseReelle":
            self.boutonSelecBaseTest.deselect()
        elif self.boutonsBaseSelect.get() == "baseTest":
            self.boutonSelectBaseReelle.deselect()


    def transformTextBaseToBool(self):
        '''
        si self.boutonsBaseSelect = baseReelle, renvoie True
        si self.boutonsBaseSelect = baseTest, renvoie False
        '''
        return self.boutonsBaseSelect.get() == "baseTest"


    def supprimeTexte(self):
        if self.errorText is not None:
            self.errorText.destroy()
            self.errorText = None


    def traiterRequete(self):
        self.root.update()
        laRequete = self.requete.get('1.0', tk.END)
        if self.boutonsBaseSelect.get() != "None":
            query(self.transformTextBaseToBool(), laRequete)

        if laRequete == "\n":
            self.traiterErreur(0)

        if self.boutonsBaseSelect.get() == "None":
            self.traiterErreur(1)


    def traiterErreur(self, numErr):
        if self.errorText:
            self.errorText.destroy()
        self.errorText = tk.Label(self.root, text="Attention : " + dicoErreur()[numErr], fg="red")
        self.errorText.place(x=100, y=110)
        self.root.after(4000, self.supprimeTexte)




    ########################################################################################################
    '''
    PARTIE SUR LES REQUETES PERMETTANT D'AFFICHER LES DONNEES SUR UN GRAPHIQUE
    '''

    def changeValeurBouton(self):
        if self.afficheTab.get():
            self.buttonTab.configure(text="Affiche tableau : OFF")
            self.afficheTab.set(False)
            
        else:
            self.buttonTab.configure(text="Affiche tableau : ON")
            self.afficheTab.set(True)
            self.afficheTabEnFonctionDonnees()
        self.resize_window()


    def resize_window(self):
        if self.afficheTab.get():
            self.root.geometry(f"{int(self.width*2.5)}x{self.height}")
        else:
            self.root.geometry(f"{self.width}x{self.height}")


    def executeBoutonTap(self):
        self.resize_window()
        self.changeValeurBouton()


    def afficheGraphiqueDonnees(self):
        #bouton permettant de voir le tab ou non en élargissant la fenetre
        self.buttonTab = tk.Button(self.root, text="Affiche tableau : OFF", command=self.executeBoutonTap)
        self.buttonTab.place(x= self.convX(160), y=270)


    def creerTab(self, abscisse, ordonnee):
        #self.afficheTabEnFonctionDonnees()
        if self.fig is None:
            #si c'est la premiere fois qu'on le trace
            self.fig = Figure(figsize=(8, 3), dpi=100)
            self.ax = self.fig.add_subplot(111)
            self.ax.plot(abscisse, ordonnee)
        else:
            #si le graph est déja tracé alors on le clear pour le retracer
            self.fig = Figure(figsize=(8, 3), dpi=100)
            self.ax.clear()
            self.ax = self.fig.add_subplot(111)
            self.ax.plot(abscisse, ordonnee)
        
        if self.afficheTab.get():
            canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            canvas.draw()
            xPlace, yPLace = self.width + 10, 0
            canvas.get_tk_widget().place(x=xPlace, y=yPLace)


    def afficheFonctionsDuTab(self):
        labelMenu1 = tk.Label(self.root, text="Agrégation :")
        labelMenu1.place(x=12, y=130)

        labelMenu2 = tk.Label(self.root, text="Abscisse :")
        labelMenu2.place(x=117, y=130)


        self.selected_option1 = tk.StringVar(self.root)
        self.selected_option1.set("Moyenne")
        self.selected_option1.trace("w", self.afficheTabEnFonctionDonnees)
        self.agreDuGraph = tk.OptionMenu(self.root, self.selected_option1, "Moyenne", "Somme", "Maximum", "Minimum")
        self.agreDuGraph.config(width=10)
        self.agreDuGraph.place(x=10, y= 150)

        self.selected_option2 = tk.StringVar(self.root)
        self.selected_option2.set("Années")
        self.selected_option2.trace("w", self.afficheTabEnFonctionDonnees)
        self.absDuGraph = tk.OptionMenu(self.root, self.selected_option2, "Années", "Région", "Département")
        self.absDuGraph.config(width=10)
        self.absDuGraph.place(x=115, y= 150)


    def afficheTabEnFonctionDonnees(self, *args):
        self.root.update()
        if self.selected_option2.get() != "Années":
            requete = f"SELECT {WORD_CONVERTOR[self.selected_option2.get()]}, {WORD_CONVERTOR[self.selected_option1.get()]}(nbHab) FROM commune c, population p WHERE c.codeG=p.codeG GROUP BY {WORD_CONVERTOR[self.selected_option2.get()]};"
        else:
            requete = f"SELECT {WORD_CONVERTOR[self.selected_option2.get()]}, {WORD_CONVERTOR[self.selected_option1.get()]}(nbHab) FROM population GROUP BY {WORD_CONVERTOR[self.selected_option2.get()]};"
        
        reponse = query(False, requete)
        abscisse = []
        ordonnee = []
        for ligne in range(len(reponse)):
            abscisse.append(reponse[ligne][0])
            ordonnee.append(reponse[ligne][1])
        
        self.creerTab(abscisse, ordonnee)




    ########################################################################################################

    '''
    PARTIE SUR L'AFFICHAGE DE LA CARTE DE FRANCE
    '''

    def afficheVilleSelect(self):
        '''
        affiche la carte de france avec les ville sélectionner dans la requete
        '''
        pass



    ########################################################################################################
    '''
    PARTIE SUR LA FERMETURE ET LA BOUCLE INFINIE DE LA FENETRE
    '''

    def boutonExit(self):
        bouton = tk.Button(self.root, text="Quiter", command=self.fermer_fenetre)
        # Affichage du bouton dans la fenêtre
        bouton.place(x=10, y=self.height-30)


    def fermer_fenetre(self):
        self.root.destroy()





def mainfenetre():
    # Créer une instance de la classe FenetreGraphique pour afficher la fenêtre
    fenetre = FenetreGraphique(500, 300)
    fenetre.lancerFenetre()

    #mise a jour des base de données
    fenetre.miseAJourBase()

    # exécution des requetes sur la base de données sélectionenner
    fenetre.requeterBase()

    fenetre.afficheGraphiqueDonnees()
    fenetre.afficheFonctionsDuTab()

    fenetre.boutonExit()
    fenetre.continuerAfficher()