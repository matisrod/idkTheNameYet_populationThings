import tkinter as tk
from dataToDB.creationBD import creationBD
from dataToDB.insertionBD import toutInserer
from dataToDB.query import query


class FenetreGraphique:
    def __init__(self):
        self.root = tk.Tk()
        self.TESTER = tk.BooleanVar()
        self.CREER = tk.BooleanVar()
        self.INSERER = tk.BooleanVar()
        self.REQUETER = tk.BooleanVar()
        self.requete = "SELECT nbhab FROM commune c, population p WHERE c.codeG=p.codeG AND dept LIKE '91' and annees = 2020"


    def lancerFenetre(self):
        ''''
        lance la fenetre au centre de l'écran
        '''
        # Obtenir la taille de l'écran
        largeur_ecran = self.root.winfo_screenwidth()
        hauteur_ecran = self.root.winfo_screenheight()

        # Calculer les coordonnées x et y pour placer la fenêtre au centre de l'écran
        x = (largeur_ecran // 2) - (400 // 2)
        y = (hauteur_ecran // 2) - (300 // 2)

        # le user ne peut pas la redimentionner
        self.root.resizable(False, False)

        # lancer la fenetre en fonction de la taille de l'écran
        self.root.geometry("400x300+{}+{}".format(x, y))

    '''
    def tracerTrait(self):
        # Créer un canvas de 400x300 pixels
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        
        # Tracer un trait rouge
        self.canvas.create_line(50, 50, 350, 250, fill="black")

        
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
    

    def traiter_entree2(self, event):
        texte = self.entry2.get()
        texte.place(x=100, y=100)
        print("Texte saisi dans le deuxième champ :", texte)
    '''

    def continuerAfficher(self):
        self.root.mainloop()


    def executerAction1(self):
        '''
        TESTER, CREER, INSERER, REQUETER en fonction des var 1, 2, 4 et 4
        '''
        self.root.update() # Met à jour l'état des cases à cocher
        print(self.TESTER.get(), self.CREER.get(), self.INSERER.get(), self.REQUETER.get())

        if self.CREER.get():
            #on cré la base de données test ou non
            creationBD(self.TESTER.get())

        if self.INSERER.get(): #données a insérer
            toutInserer(self.TESTER.get())

        if self.REQUETER.get():
            #la requête a exectuter
            query(self.TESTER.get(), self.requete)

    
    def traiterDemande(self):
        '''
        demander avec des bouton si oui ou non le user veut : TESTER, CREER, INSERER, REQUETER
        '''
        #créer un cadre pour entourer le tout
        cadre = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        cadre.place(x=10, y=10)
        cadre.config(width=150, height=140)

        checkbutton1 = tk.Checkbutton(cadre, text="Base de test", variable=self.TESTER)
        checkbutton1.place(x=10,y=10)

        checkbutton1 = tk.Checkbutton(cadre, text="Créer/Recréer base", variable=self.CREER)
        checkbutton1.place(x=10,y=30)

        checkbutton1 = tk.Checkbutton(cadre, text="Insérer base", variable=self.INSERER)
        checkbutton1.place(x=10,y=50)

        checkbutton1 = tk.Checkbutton(cadre, text="Requeter base", variable=self.REQUETER)
        checkbutton1.place(x=10,y=70)

        bouton = tk.Button(cadre, text="Mettre à jour", command=lambda: self.executerAction1(), state="normal")
        bouton.place(x=35, y=100)


    def boutonExit(self):
        bouton = tk.Button(self.root, text="Quiter", command=self.fermer_fenetre)
        # Affichage du bouton dans la fenêtre
        bouton.place(x=350, y=270)


    def fermer_fenetre(self):
        self.root.destroy()



def mainfenetre():
    # Créer une instance de la classe FenetreGraphique pour afficher la fenêtre
    fenetre = FenetreGraphique()
    fenetre.lancerFenetre()
    fenetre.traiterDemande()
    fenetre.boutonExit()
    fenetre.continuerAfficher()