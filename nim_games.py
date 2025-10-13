#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

"""
Jeu de Nim (variante simple) - 21 allumettes
"""

def demander_mode_jeu():
    while True:
        mode = input("Tapez SIMPLE (mode classique) ou MARIENBAD (non disponible pour l'instant) : ").strip().upper()
        if mode == "SIMPLE":
            return mode
        elif mode == "MARIENBAD":
            print("Le mode MARIENBAD n'est pas encore disponible.")
        else:
            print("Veuillez taper SIMPLE.")

def demander_type_de_partie():
    while True:
        choix = input("Tapez ORDINATEUR ou JOUEUR : ").strip().upper()
        if choix == "JOUEUR":
            nom1 = input("Entrez le nom du joueur 1 : ")
            nom2 = input("Entrez le nom du joueur 2 : ")
            return [nom1, nom2]
        elif choix == "ORDINATEUR":
            nom1 = input("Entrez le nom du joueur : ")
            return [nom1, "Ordinateur"]
        else:
            print("Choix invalide. Tapez ORDINATEUR ou JOUEUR.")

def tour_joueur(nom, allumettes_restantes):
    while True:
        try:
            prise = int(input(f"{nom}, combien d'allumettes voulez-vous prendre ? (1 à 4) : "))
            if 1 <= prise <= 4 and prise <= allumettes_restantes:
                return prise
            else:
                print("Veuillez entrer un nombre entre 1 et 4, sans dépasser les allumettes restantes.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def tour_ordinateur(dernier_choix_joueur, allumettes_restantes):
    # Stratégie basique : réponse complémentaire à 5 si possible
    if dernier_choix_joueur:
        prise = 5 - dernier_choix_joueur
    else:
        prise = random.randint(1, min(4, allumettes_restantes))

    prise = min(prise, allumettes_restantes)
    print(f"L'ordinateur prend {prise} allumette(s).")
    return prise

def main():
    ALLUMETTES_INITIALES = 21
    allumettes = ALLUMETTES_INITIALES

    mode = demander_mode_jeu()
    joueurs = demander_type_de_partie()

    # Tirage au sort du premier joueur
    joueur_actuel = random.randint(0, 1)
    print(f"\n{joueurs[joueur_actuel]} commence la partie.\n")

    dernier_choix = None

    while allumettes > 0:
        print(f"\nAllumettes restantes : {allumettes}")
        nom_joueur = joueurs[joueur_actuel]

        if nom_joueur != "Ordinateur":
            prise = tour_joueur(nom_joueur, allumettes)
            dernier_choix = prise
        else:
            prise = tour_ordinateur(dernier_choix, allumettes)

        allumettes -= prise

        if allumettes == 0:
            print(f"\n{nom_joueur} a pris la dernière allumette et perd la partie.")
            gagnant = joueurs[1 - joueur_actuel]
            print(f"{gagnant} gagne !\n")
            break

        joueur_actuel = 1 - joueur_actuel

# Lancement du jeu
if __name__ == "__main__":
    main()
