# Projet des Populations en France

1. Explications
2. Lancement
3. Annexes


## 1. Explications

Ce projet à pour but de d'étudier l'évolution de la population en France au fil des années (environ de 1876 à 2020). De plus celui-ci me permetera d'obtenir les valeurs foncieres des années 2017 à 2022. Cela correspond a obtenir tous les achats de terrains en france pour une année sur 6 ans. Il sera donc possible d'effetuer certains calculs statistiques sur ces informations.

## 2. Lancement

Tout ce qui suit correspond à ce qui a été réalisé jusqu'à aujourd'hui. Il se peut que cela change.

1. Certains fichiers sont trop volumineux pour etre posés ici
2. Pour démarrer le programme :
    * Il faut lancer le fichier situer dans _/main/src/main.py_ 
    * Il y a 4 variables de lancement à disposition : TESTER, CREER, INSERER, REQUETER. 
    * C'est variable permete dans l'ordre d'effectuer les actions suivantes :
        * Si ***TESTER=True***, alors nous sommes en phase de test, sinon, c'est que l'on s'apprête a réaliser les actions suivantes avec la véritable base de données.
        * Si ***CREER=True***, alors je crée une base de données en fonction du paramètre __TESTER__
        * Si ***INSERER=True***, alors j'insere les données présentes dans les fichier de tests ou non toujours en fonction de mon paramètre __TESTER__
        * Si ***REQUETER=True***, alors j'exécute la requête passée en argument sur la base de données choisie grâce a __TESTER__
    * Exemple au lancement : Je souhaite lancer la vraie base de données. Je mets donc __TESTER=True__, __CREER=True__, __INSERER=True__ et __REQUETER__ n'est pas important pour l'instant. Puis une fois le programme exécuter, je peux mettre __CREER__ et __INSERER__ sur False car la base vient d'être créée. Je laisse cependant __TESTER=True__ car c'est lui qui indique sur quelle base de donnée la requête va être exécutée. Puis pour la requête il suffit de tester n'importe quelle requête fonctionnelle en SQL.


## 3. Annexes
