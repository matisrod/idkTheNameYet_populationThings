import sqlite3
from textToData.basePopulationExploitation import creerDonneesBasePopulation
from textToData.laposteHexaExploitation import creerDonneesLaposteHexa

ALERTES = False

class Database:

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def insert_data(self, table_name, data):
        '''
        permet d'insérer des valeurs dans la DB
        '''
        keys = ', '.join(data.keys())
        values = ', '.join(['?' for _ in range(len(data.values()))])
        request = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
        self.cur.execute(request, tuple(data.values()))
        self.conn.commit()
        if ALERTES:
            print("Data inserted successfully!")
    

    def update_data(self, table_name, new_data, condition):
        """
        permet d'update une table précise avec de nouvelle donnée
        """
        set_clause = ", ".join([f"{key} = ?" for key in new_data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        parameters = tuple(new_data.values())
        self.cur.execute(query, parameters)
        self.conn.commit()
        if ALERTES:
            print("Data updated successfully!")
        

    def close_connection(self):
        '''
        fermeture du curseur et de la connection
        '''
        self.cur.close()
        self.conn.close()


nomTablesAttributs = {
    "Commune" : ["codeG", "reg", "dept", "lib", "lat", "long"],
    "Population" : ["annees", "nbHab", "codeG"]
    }


def suppressionDoublon(donneesLaposteHexa):
    newDicLaposteHexa = {}
    for ligne in donneesLaposteHexa:
        key = ligne[0]
        if key not in newDicLaposteHexa:
            newDicLaposteHexa[key] = ligne
    donneesLaposteHexa = list(newDicLaposteHexa.values())
    return donneesLaposteHexa


def insererPremieresDonnees(donneesBasePop, TEST):
    if TEST:
        db = Database('projetPopulationTEST.db')
    else:
        db = Database('projetPopulation.db')

    for nLigne in range(1, len(donneesBasePop)):
        data = {}
        for x in range((len(nomTablesAttributs["Commune"])-2)):
            data[nomTablesAttributs["Commune"][x]] = donneesBasePop[nLigne][x]
        db.insert_data("Commune", data)
    print("Insertion commune is done !")
    db.close_connection()


def insererCoords(donneesLaposteHexa, TEST):
    if TEST:
        db = Database('projetPopulationTEST.db')
    else:
        db = Database('projetPopulation.db')

    donneesLaposteHexa = suppressionDoublon(donneesLaposteHexa)
    for ligne in range(1, len(donneesLaposteHexa)):
        latitude, longitude = donneesLaposteHexa[ligne][-2], donneesLaposteHexa[ligne][-1]
        data = {nomTablesAttributs["Commune"][-2] : latitude, nomTablesAttributs["Commune"][-1] : longitude}
        condition = f"codeG LIKE '{donneesLaposteHexa[ligne][0]}'"
        db.update_data("Commune", data, condition)
    print("Insertion coords is done !")
    db.close_connection()
    

def toutInserer(donneesBasePop, donneesLaposteHexa, TEST):
    insererPremieresDonnees(donneesBasePop, TEST)
    insererCoords(donneesLaposteHexa, TEST)


def mesDonnes(TEST):
    donneesBasePop = creerDonneesBasePopulation(TEST)
    donneesLaposteHexa = creerDonneesLaposteHexa(TEST)
    return donneesBasePop, donneesLaposteHexa