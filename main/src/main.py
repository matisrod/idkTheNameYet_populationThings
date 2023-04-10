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
        
    

    if INSERER:
        #extraction données des fichiers :
        donneesBasePop, donneesLaposteHexa = mesDonnes(TESTER)

        #inserer toutes les info : codeGeographique, region, departement, libelleGeo, latitude, longitude

        #insererPremieresDonnees(donneesBasePop, TESTER)
        #insererCoords(donneesLaposteHexa, TESTER)
        #insertionPopulation(TESTER, donneesBasePop)
        toutInserer(donneesBasePop, donneesLaposteHexa, TESTER)
        
        
    if REQUETER:
        #votre requete :
        # exemple : on donne le nom de toute les villes avec leur nombred'habitant en 2020
        query(TESTER, "select lib, nbHab from commune c, population p WHERE c.codeG=p.codeG AND annees = 2020")
        