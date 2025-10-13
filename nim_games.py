#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
"""
Jeu de Nim (variante simple et de Marienbad)
"""
number_matches = 21
number_of_choose_matches = None

#Choix du mode de jeu (Ordinateur ou Joueur)
while True:
    type_of_game = input("Tapez ORDINATEUR ou JOUEUR : ").strip().upper()

    #Si le choix est Joueur
    if type_of_game == "JOUEUR":
        name_player_1 = input("Entrez le nom du joueur 1 : ")
        name_player_2 = input("Entrez le nom du joueur 2 : ")
        players = [name_player_1, name_player_2]
        break

    #Si le choix est Ordinateur
    elif type_of_game == "ORDINATEUR":
        name_player_1 = input("Entrez le nom du joueur : ")
        name_player_2 = "Ordinateur"
        players = [name_player_1, name_player_2]
        break

    else:
        print("Veuillez taper ORDINATEUR ou JOUEUR.")

#Choisis aléatoirement qui commence la partie
current_player_index = random.randint(0, 1)
print(f"\n{players[current_player_index]} commence la partie.\n")

#Boucle tant qu'il reste des allumettes
while number_matches > 0:
    print(f"\nAllumettes restantes : {number_matches}")
    current_player = players[current_player_index]

    #Si joueur contre joueur
    if current_player != "Ordinateur":
        while True:
                number_of_choose_matches = int(input(f"{current_player}, combien d'allumettes voulez-vous prendre ? (1 à 4) : "))
                if 1 <= number_of_choose_matches <= 4 and number_of_choose_matches <= number_matches:
                    break
                else:
                    print("Veuillez entrer un nombre entre 1 et 4 sans dépasser le nombre d'allumettes restantes")
    else:
        if number_of_choose_matches is None:
            number_of_choose_matches = random.randint(1, 4)
        else:
            number_of_choose_matches = 5 - number_of_choose_matches
            print(f"Ordinateur prend {number_of_choose_matches} allumette(s)")


    number_matches -= number_of_choose_matches

    if number_matches == 0:
        print(f"\n{current_player} perd la partie.")
        winner = players[1 - current_player_index]
        print(f"{winner} gagne !")
        break

    current_player_index = 1 - current_player_index