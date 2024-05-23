# Jeu du pendu

Dans le cadre du cours MGA802 à la session d'été de l'ETS. 

Ce code a pour fonction de :

    Sélectionner un mot aléatoire à partir d’un fichier texte contenant un grand nombre de mots fournis dans le GitHub.
    (! Attention ! Ce fichier est à enregistrer dans le même fichier que le code.)
    Faire tourner une boucle tant que le nombre de chances (fixé initialement à 6) de l’utilisateur est supérieur à zéro
    À chaque boucle, le programme va:

    Afficher l’état actuel des mots en utilisant des _ pour les lettres non devinées
    Demander à l’utilisateur d’entrer une lettre
    Indiquer à l’utilisateur si la lettre faisait partie du mot ou pas
    Mettre à jour les chances si nécessaires et, si c’est le cas:

    Indiquer à l’utilisateur s’il a gagné
    Indiquer à l’utilisateur s’il a perdu

    Boucler.

De plus :

    L’utilisateur peut fournir son propre fichier « mots_pendu.txt », sinon le fichier par défaut va être sélectionné.
    Les mots contenant des lettres avec des accents (é è ê à â û …) sont reliées à leurs équivalent sans accents (e a u …)
    Si l’utilisateur perd ou gagne, le programme propose à l’utilisateur de recommencer ou quitter.
    L'utilisateur peut mettre à jours le nombre d'essais à chaque partie. 

! Attention aux majuscules dans les mots ! 

    Il n'y en a pas dans le fichier par défaut, mais le code fait la différence entre la majuscule et la minuscule.
    Ainsi 'A' est différent de 'a' pour le jeu.

Lorsque l'adresse du fichier doit être fournis merci de le faire pour chaque élément sous la forme décrite :

    - chemin, ex : C:\User\Jeu
    - fichier, ex : mots_pendu
    le code crée automatiquement une adresse 'C:\User\Jeu\mots_pendu.txt'

# Amusez vous bien !
