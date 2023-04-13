import sqlite3
import os

def creationBD(TEST):
    # Connectez-vous à la base de données
    print(TEST)
    if TEST:
        db_file = "projetPopulationTEST.db"
        NEW_DB = os.path.exists(db_file)
        conn = sqlite3.connect(db_file)
    else:
        db_file = "projetPopulation.db"
        makeSureToDelete = input("Etes vous sûr de vouloir detruire la réelle DB (Y / N) ?")
        if makeSureToDelete in ["y", "Y"]:
            NEW_DB = os.path.exists(db_file)
            conn = sqlite3.connect(db_file)
        else:
            print("REFUS DE CRÉATION")
            return #cela veut dire que l'on a rien fait

    # Créez un curseur pour exécuter des requêtes SQL
    cur = conn.cursor()
    
    if NEW_DB:
        # suppression de la table Commune car elle existe deja
        cur.execute("DROP TABLE Commune;")

    #creation de la table Commune
    cur.execute('''CREATE TABLE Commune(
                codeG varchar(5) PRIMARY KEY,
                reg varchar(5) NOT NULL,
                dept varchar(5) NOT NULL,
                lib TEXT NOT NULL,
                lat float,
                long float);''')

    if NEW_DB:
        # suppression de la table population car elle existe deja
        cur.execute("DROP TABLE Population;")

    # création de la table population
    cur.execute('''CREATE TABLE Population(
                annees int NOT NULL CHECK(annees >= 1876),
                nbHab int NOT NULL CHECK(nbHab >= 0),
                codeG int REFERENCES Commune,
                PRIMARY KEY(codeG, annees));''')


    #sauvegarde des données dans la BD
    conn.commit()

    #fermeture du cursseur et de la connextion
    cur.close()
    conn.close()
    
    #si on arrive ici, c'est que tout c'est bien passé