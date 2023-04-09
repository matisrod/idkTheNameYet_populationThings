import sqlite3

def query(TEST, commande, SAUV = True):
    if TEST:
        # Connectez-vous à la base de données
        conn = sqlite3.connect('projetPopulationTEST.db')
    else:
        conn = sqlite3.connect('projetPopulation.db')

    # Créez un curseur pour exécuter des requêtes SQL
    cur = conn.cursor()

    # on execute une commande, que l'on met dans le cursseur, on peut apres le parcourir et afficher les ligne
    # avec une simple boucle ou alors le fetchall pour mettre les info ds une liste

    cur.execute(commande)

    donnees = cur.fetchall()

    # on regarde si on a des lignes a donner
    if donnees is None:
        print("Aucune ligne relevée")
    else:
        # on affiche chaque ligne de ma requete
        for i in donnees:
            print(i)
        print()

    if SAUV:
        #sauvegarde des données dans la BD
        conn.commit()

    #fermeture du cursseur et de la connextion
    cur.close()
    conn.close()