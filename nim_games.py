#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

"""
Jeu de Nim (variante simple) - 21 allumettes
"""

def ask_game_mode():
    while True:
        game_mode = input("Tapez SIMPLE (mode classique) ou MARIENBAD (non disponible pour l'instant) : ").strip().upper()
        if game_mode == "SIMPLE":
            return game_mode
        elif game_mode == "MARIENBAD":
            print("Le mode MARIENBAD n'est pas encore disponible.")
        else:
            print("Veuillez entre SIMPLE ou MARIENBAD")

def ask_type_of_game():
    while True:
        choice = input("Tapez ORDINATEUR ou JOUEUR : ").strip().upper()
        if choice == "JOUEUR":
            player_name_1 = input("Entrez le nom du joueur 1 : ")
            player_name_2 = input("Entrez le nom du joueur 2 : ")
            return [player_name_1, player_name_2]
        elif choice == "ORDINATEUR":
            player_name_1 = input("Entrez le nom du joueur : ")
            return [player_name_1, "Ordinateur"]
        else:
            print("Choix invalide. Tapez ORDINATEUR ou JOUEUR.")

def player_turn(name, matches_remaining):
    while True:
            number_of_matches_choose = int(input(f"{name}, combien d'allumettes voulez-vous prendre ? (1 à 4) : "))
            if 1 <= number_of_matches_choose <= 4 and number_of_matches_choose <= matches_remaining:
                return number_of_matches_choose
            else:
                print("Veuillez entrer un nombre entre 1 et 4, sans dépasser les allumettes restantes.")

def computer_turn(last_choice_player, matches_remaining):
    # Stratégie basique : réponse complémentaire à 5 si possible
    if last_choice_player:
        number_of_matches_choose = 5 - last_choice_player
    else:
        number_of_matches_choose = random.randint(1, min(4, matches_remaining))

    number_of_matches_choose = min(number_of_matches_choose, matches_remaining)
    print(f"L'ordinateur prend {number_of_matches_choose} allumette(s).")
    return number_of_matches_choose

def main():
    number_matches = 21
    matches = number_matches

    mode = ask_game_mode()
    players = ask_type_of_game()

    # Tirage au sort du premier joueur
    actual_player = random.randint(0, 1)
    print(f"\n{players[actual_player]} commence la partie.\n")

    last_choice = None

    while matches > 0:
        print(f"\nAllumettes restantes : {matches}")
        player_name = players[actual_player]

        if player_name != "Ordinateur":
            number_of_matches_choose = player_turn(player_name, matches)
            last_choice = number_of_matches_choose
        else:
            number_of_matches_choose = computer_turn(last_choice, matches)

        matches -= number_of_matches_choose

        if matches == 0:
            print(f"\n{player_name} a pris la dernière allumette et perd la partie.")
            winner = players[1 - actual_player]
            print(f"{winner} gagne !\n")
            break

        actual_player = 1 - actual_player

# Lancement du jeu
if __name__ == "__main__":
    main()
