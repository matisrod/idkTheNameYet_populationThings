from dataToDB.creationBD import creationBD
from dataToDB.insertionBD import toutInserer, insererPremieresDonnees ,insererCoords, mesDonnes, insertionPopulation
from dataToDB.query import query

TESTER = True # TRUE = JE FAIS DES TESTS
CREER = True # JE CRÉER UNE DB
INSERER = True # J'INSERE DANS MA DB
REQUETER = True # je fais une requete a ma DB

if __name__ == "__main__":
    if CREER:
        #création d'une base de données de test :
        creation = creationBD(TESTER)
        
    #extraction données des fichiers :
    donneesBasePop, donneesLaposteHexa = mesDonnes(TESTER)

    if INSERER:
        #inserer toutes les info : codeGeographique, region, departement, libelleGeo, latitude, longitude

        #insererPremieresDonnees(donneesBasePop, TESTER)
        #insererCoords(donneesLaposteHexa, TESTER)
        toutInserer(donneesBasePop, donneesLaposteHexa, TESTER)
        insertionPopulation(TESTER, donneesBasePop)
        
        
    if REQUETER:
        #votre requete :
        #query(TESTER, "select * from commune")
        query(TESTER, "select * from population")
        