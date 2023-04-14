import sqlite3


def query(TEST, commande):
    assert commande!= "\n", f"La comamnde de la requete est vide."

    if TEST:
        # Connectez-vous à la base de données
        conn = sqlite3.connect('projetPopulationTEST.db')
    else:
        conn = sqlite3.connect('projetPopulation.db')

    # Créez un curseur pour exécuter des requêtes SQL
    cur = conn.cursor()

    # on execute une commande, que l'on met dans le cursseur, on peut apres le parcourir et afficher les ligne
    # avec une simple boucle ou alors le fetchall pour mettre les info ds une liste
    print("Requête : " + commande)
    cur.execute(commande)

    donnees = list(cur.fetchall())

    # on regarde si on a des lignes a donner
    if donnees == []:
        pass
        #print("Aucune ligne relevée")
    else:
        # on affiche chaque ligne de ma requete
        for i in donnees:
            print(i)

    #fermeture du cursseur et de la connextion
    cur.close()
    conn.close()

    return donnees