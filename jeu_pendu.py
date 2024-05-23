# Ce programme est un jeu du pendu.
# Le programme propose de trouver un mot à partir d'un fichier de mots.
# Le fichier peut être importé ou un fichier existant dans le GitHub est déjà disponible.


import random
import unicodedata
import os


# Réalise les étapes du jeu à partir d'un mot et du nombre d'essais en donnant l'avancée
def trouver_mot(mot, nbre_essais=6):
    mot_vide = ['_' for _ in range(len(mot))]  # Table du mot sans les lettres
    lst_mot = [mot[i] for i in range(len(mot))]  # Table du mot avec les lettres
    i = nbre_essais
    nbr_lettres_restantes = len(mot)
    lettres_util = []  # Table pour les lettres utilisées lors de la partie
    while i > 0:  # boucle sur le nombre de vie restantes
        lettre = input(f"Quelle lettre choisissez vous ?   ")
        if trouver_lettre(lettre, lst_mot):  # vérifie que la lettre est dans le mot et l'ajoute au mot vide
            [mot_vide, nbr_lettres_restantes] = changer_lettre(lettre, mot_vide, lst_mot, nbr_lettres_restantes)
            print("Bravo ! La lettre est ajoutée, nous avons maintenant :\n"
                  f"{mot_vide}\n")
            lettres_util.append(lettre)
            print(f"Il reste {i}/{nbre_essais} essais\n"
                  f"Rappel des lettres utilisées : {lettres_util}\n")
            if nbr_lettres_restantes == 0:  # Si toutes les lettres on été trouvées le jeu se fini et propose de recommencer
                print(f"Bravo ! Vous avez trouvé le mot '{mot}'.")
                recommencer()
        else:  # la lettre n'est pas dans le mot, perte d'une vie
            print("Dommage :( . La lettre n'est pas dans le mot\n"
                  f"Pour rappel nous avons {mot_vide}")
            lettres_util.append(lettre)
            i -= 1
            print(f"Il reste {i}/{nbre_essais} essais\n"
                  f"Rappel des lettres utilisées : {lettres_util}\n")
    print(f"Le mot était : {mot}")
    recommencer()


# Verifie si la lettre choisi par le joueur est dans la table contenant les lettres du mot
def trouver_lettre(lettre, lst_mot):  # fonction verifier que la lettre est dans le mot
    for i in range(len(lst_mot)):
        if lst_mot[i] == lettre:
            return True
    return False


# Change la lettre choisi par l'utilisateur dans la table du mot blanc à remplir
# Ex : si des 'e' dans le mot ['_','_','_','_','_','_','_','_'] devient ['_','e','_','_','_','e','_','_']
# Retourne également le nombre de lettres à trouver
def changer_lettre(lettre, mot_vide, lst_mot, nbr_lettres_restantes):  # fonction ajouter la lettre dans le mot vide
    for i in range(len(lst_mot)):
        if lst_mot[i] == lettre:
            mot_vide[i] = lettre
            nbr_lettres_restantes -= 1
    return [mot_vide, nbr_lettres_restantes]


# Permet de relancer le jeu avec de nouveaux paramètres après chaque partie
def recommencer():
    ask_restart = input(f"Voulez vous reessayer avec un autre mot ?\n Oui/Non   ")
    if ask_restart == "Oui" or ask_restart == "oui":
        new_mot = donner_mot()
        ask_nbre_essais = input(f"Voulez vous changer le nombre d'essais possibles ?\n Oui/Non   ")
        if ask_nbre_essais == "Oui" or ask_nbre_essais == "oui":
            nbre_essais = int(input(f"Entrez le nombre d'essais souhaités pour cet essais :   "))
            trouver_mot(new_mot, nbre_essais)
        else:
            trouver_mot(new_mot)
    else:
        print("Merci d'avoir joué. A bientôt!")
        quit()


# Permet d'importer un mot aléatoire soit dans le fichier utilisateur ou le fichier par défaut
def donner_mot():
    ask_trouver_fichier = input(f"Voulez vous importer les mots d'un de vos fichier .txt ?\nOui/Non   ")
    if ask_trouver_fichier == "Oui" or ask_trouver_fichier == "oui":  # lance le code pour que le joueur puisse choisir son fichier
        ask_chemin_fichier = input(f"Quel est l'emplacement du fichier ? :  ")  # donné sous la forme emplacement sur windows, ex : C:\Users\Documents
        ask_nom_fichier = input(f"Quel est le nom du fichier ? :   ")  # juste le titre, ex : fichier_de_mots
        chemin = ask_chemin_fichier + os.sep + ask_nom_fichier + '.txt'  # créer le chemin du fichier
        test_chemin = os.path.isfile(chemin)  # vérifie que le fichier existe au bon endroit
        if test_chemin:
            return choisir_mot(chemin)  # retourne un mot aléatoire dans le fichier utilisateur
    else:
        print("Le fichier n'est pas à l'endroit décrit. La partie est lancée avec un mot par défaut.")
        return choisir_mot()  # retourne un mot aléatoire dans le fichier par défaut


# Permet d'importer un mot aléatoire dans un fichier .txt dont le chemin est fourni en entrée
def choisir_mot(chemin="mots_pendu.txt"):
    with open(chemin, "r", encoding='utf-8') as text_file:  # Ouvre en lecture le fichier dont on a donné le chemin
        lines = text_file.read().split()  # sépare les mots dans le fichier
        lines_decode = []
        for line in lines:  # crée une table avec les mots du fichier
            lines_decode.append(unicodedata.normalize('NFD', line).encode('ascii', 'ignore').decode("utf-8"))
    return random.choice(lines_decode)  # retourne un mot aléatoire de la table


# Texte et lancement de la fonction jeu.
print("Bonjour, ce code permet de jouer au 'Jeu du pendu'.\n"
      "Vous avez la possibilité d'importer votre propre set de mot.\n"
      "Pour cela donnez dans les phases suivantes l'accés au fichier sous la forme :\n"
      r"Chemin = C:\User et Nom = Fichier " + "\nLe code s'occupera du reste.\nAmusez vous bien !")
trouver_mot(donner_mot())
