from dataToDB.creationBD import creationBD
from dataToDB.insertionBD import toutInserer, insererPremieresDonnees ,insererCoords, mesDonnes, insertionPopulation
from dataToDB.query import query
from graphics.CarteFrance import AffichageCarteFrance

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
        #query(TESTER, "select lib, nbhab from commune c, population p WHERE (c.codeG = p.codeG) AND (lib LIKE 'ajaccio%' OR lib LIKE 'bastia%') AND annees = 2020")

        
        #votre requete :
        reponse = query(TESTER, "select lib, lat, long from commune WHERE dept LIKE '01' AND long is not null")
        data = {reponse[x][0] : [reponse[x][y] for y in range(1, len(reponse[0]))] for x in range(len(reponse))}
        maMarte = AffichageCarteFrance(data)
        maMarte.creationCarte()


        # exemple : donne les extrems de la france métropolitaine, la corse exclue : (fonctionne si on a toutes les données des coords dans notre base)
        reponse = query(TESTER, '''select max(lat), min(lat), max(long), min(long) from commune 
                         WHERE (codeG LIKE '01_%' OR codeG LIKE '1_%' 
                                                 OR codeG LIKE '2_%' OR codeG LIKE '3_%' OR codeG LIKE '4_%' 
                                                 OR codeG LIKE '5_%' OR codeG LIKE '6_%' OR codeG LIKE '7_%' 
                                                 OR codeG LIKE '8_%' OR codeG LIKE '91_%'
                                                 OR codeG LIKE '92_%' OR codeG LIKE '93_%'
                                                 OR codeG LIKE '94_%' OR codeG LIKE '95_%')
                                                 AND NOT --on exclue ici la Corse
                                                 (codeG LIKE '2A_%' OR codeG LIKE '2B_%')''')