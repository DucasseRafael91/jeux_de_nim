#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim (variante simple et de Marienbad)
"""
import random

while True:
    typeofgame = input("Tapez ORDINATEUR ou JOUEUR : ")

    if typeofgame == "JOUEUR":
        nameplayer1 = input("Entrez le nom du joueur 1 : ")
        nameplayer2 = input("Entrez le nom du joueur 2 : ")

        starter = random.randint(1, 2)

        if starter == 1:
            print(f"{nameplayer1} commence la partie.")
        else:
            print(f"{nameplayer2} commence la partie.")
        break

    elif typeofgame == "ORDINATEUR":
        nameplayer1 = input("Entrez le nom du joueur : ")
        print(f"{nameplayer1} va jouer contre l'ordinateur.")
        break

    else:
        print("Entrée invalide. Veuillez taper ORDINATEUR ou JOUEUR.")
