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
    '''
    suppresion des doublon dans laposteHexa
    '''
    newDicLaposteHexa = {}
    for ligne in donneesLaposteHexa:
        key = ligne[0]
        if key not in newDicLaposteHexa:
            newDicLaposteHexa[key] = ligne
    donneesLaposteHexa = list(newDicLaposteHexa.values())
    return donneesLaposteHexa


def insererPremieresDonnees(donneesBasePop, db):
    '''
    on insere dans Commune les attributs suivants : codeG, reg, dept et lib
    '''
    for nLigne in range(1, len(donneesBasePop)):
        data = {}
        if nLigne%250 == 0:
            db.conn.commit()
            if nLigne%1000 == 0:
                print("Ligne " + str(nLigne) + "de Base Population") 

        for x in range((len(nomTablesAttributs["Commune"])-2)):
            data[nomTablesAttributs["Commune"][x]] = donneesBasePop[nLigne][x]
        db.insert_data("Commune", data)
    db.conn.commit()


def insererCoords(donneesLaposteHexa, db):
    '''
    on update la table Commune afin d'y inserer la latitute et la longitude au codeG correspondant 
    '''
    donneesLaposteHexa = suppressionDoublon(donneesLaposteHexa)
    for ligne in range(1, len(donneesLaposteHexa)):
        if ligne%280 == 0:
            db.conn.commit()
            if ligne%1120 == 0:
                print("Ligne " + str(ligne) + "de Base Population") 
        latitude, longitude = donneesLaposteHexa[ligne][-2], donneesLaposteHexa[ligne][-1]
        data = {nomTablesAttributs["Commune"][-2] : latitude, nomTablesAttributs["Commune"][-1] : longitude}
        condition = f"codeG LIKE '{donneesLaposteHexa[ligne][0]}'"
        db.update_data("Commune", data, condition)
    db.conn.commit()


def insertionPopulation(donneesBasePop, db):
    '''
    on insere dans la table population les données présentent dans donneesBasePop
    '''
    nbElt = len(donneesBasePop[0])
    annees = [donneesBasePop[0][x] for x in range(4, nbElt)]
    annees[-1] = int(annees[-1].replace("\n", ""))
    for ligne in range(1, len(donneesBasePop)):
        if ligne%35 == 0:
            db.conn.commit()
            if ligne%1400 == 0:
                print("Ligne " + str(ligne) + "de Base Population") 
        for nbPopulation in range(4, nbElt):
            annee = annees[nbPopulation-4]
            populationAnneeN = donneesBasePop[ligne][nbPopulation]
            codeG = donneesBasePop[ligne][0]
            dataAInserer = [annee, populationAnneeN, codeG]

            data = { nomTablesAttributs["Population"][x] : dataAInserer[x] for x in range( len(nomTablesAttributs["Population"]) ) }
            db.insert_data("Population", data)
    db.conn.commit()


def mesDonnes(TEST):
    '''
    renvoie sous forme de liste les données extraits des documents textes
    '''
    donneesBasePop = creerDonneesBasePopulation(TEST)
    donneesLaposteHexa = creerDonneesLaposteHexa(TEST)
    return donneesBasePop, donneesLaposteHexa


def toutInserer(TEST):
    '''
    on insere tout en meme temps : codeG, reg, dept et lib, lat et long dans commune. Puis annees, chHab et codeG dans population
    '''
    #connection a la base de test ou non
    if TEST:
        db = Database('projetPopulationTEST.db')
    else:
        db = Database('projetPopulation.db')

    donneesBasePop, donneesLaposteHexa = mesDonnes(TEST)
    insererPremieresDonnees(donneesBasePop, db)
    insererCoords(donneesLaposteHexa, db)
    insertionPopulation(donneesBasePop, db)
    db.close_connection()