from dataToDB.creationBD import creationBD
from dataToDB.insertionBD import toutInserer, insererPremieresDonnees ,insererCoords, mesDonnes, insertionPopulation
from dataToDB.query import query
from graphics.CarteFrance import AffichageCarteFrance
from graphics.FenetreDesParametres import mainfenetre

TESTER = False # TRUE = JE FAIS DES TESTS
CREER = False # JE CRÉER UNE DB
INSERER = False # J'INSERE DANS MA DB
REQUETER = True # je fais une requete a ma DB

if __name__ == "__main__":
    mainfenetre()
    '''
    if CREER:
        #création d'une base de données de test :
        creation = creationBD(TESTER)
        

    if INSERER:
        #inserer toutes les info : codeGeographique, region, departement, libelleGeo, latitude, longitude

        #insererPremieresDonnees(donneesBasePop, TESTER)
        #insererCoords(donneesLaposteHexa, TESTER)
        #insertionPopulation(TESTER, donneesBasePop)
        toutInserer(TESTER)
        
        
    if REQUETER:
        #query(TESTER, "select lib, nbhab from commune c, population p WHERE (c.codeG = p.codeG) AND (lib LIKE 'ajaccio%' OR lib LIKE 'bastia%') AND annees = 2020")

        
        #votre requete :
        reponse = query(TESTER, "select lib, lat, long from commune WHERE dept LIKE '01' AND long is not null")
        data = {reponse[x][0] : [reponse[x][y] for y in range(1, len(reponse[0]))] for x in range(len(reponse))}
        maMarte = AffichageCarteFrance(data)
        maMarte.creationCarte()
    '''