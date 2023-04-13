import geopandas as gpd
import pyproj
import matplotlib.pyplot as plt
from dataToDB import creationBD, insertionBD, query


class AffichageCarteFrance:
    '''
    affiche la carte de france avec les ville donnée dans le constructeur d'une certaine couleur
    '''
    def __init__(self, data):
        self.data = data
        

    def regionDeFrance(self):
        '''
        exécute le fichier contenant toutes les infos concertant les coordonnées de toutes les régions françaises
        '''
        regions = gpd.read_file("main/textFiles/regionCoords/regions-20180101.shp").to_crs(epsg=2154) # projection sous Lambert 93
        # on ne prend pas les régions en dehors du "réel téritoire" français
        return regions.query("nom not in ['La Réunion', 'Martinique', 'Guadeloupe', 'Guyane', 'Mayotte']")
        

    def gpsToLambert(self, coords):
        '''
        renvoie les coords passées en arguments sous Lambert 93
        '''
        lat, long = coords
        # Transformation des coordonnées GPS 
        crs_wgs = pyproj.CRS('EPSG:4326')
        crs_lambert93 = pyproj.CRS('EPSG:2154') # => (en Lambert 93)
        project = pyproj.Transformer.from_crs(crs_wgs, crs_lambert93, always_xy=True)
        x, y = project.transform(long, lat) # c'est pyproj qui prend sous long, lat
        return (x, y)

    
    def integrationPoints(self, ax):
        '''
        on rajoute des points sur la carte avec les coordonnées des villes dans self.data
        '''
        for ville in self.data:
            x, y = self.gpsToLambert(self.data[ville])
            ax.plot(x, y, marker='.', color='red')


    def creationCarte(self):
        '''
        création de la carte celon lefichier shp reçu
        '''
        regionSelectionnees = self.regionDeFrance()
        # prends les coords extrem enregistrées dans le fichier
        #xmin, ymin, xmax, ymax = regionSelectionnees.total_bounds

        fig, ax = plt.subplots(figsize=(8, 7))
        regionSelectionnees.plot(ax=ax, color='white', edgecolor='black')
        
        # on met tous les points présents sur la carte
        self.integrationPoints(ax)

        #on rend un meilleur affichage : 
        ax.axis('off')
        # Désactiver l'affichage des coordonnées
        ax.format_coord = lambda x, y: ''
        #zoom de la carte
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

        # Affichage de la carte
        plt.show()