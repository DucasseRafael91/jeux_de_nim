#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim (variante simple et de Marienbad)
"""
import random  # Importation correcte du module

nameplayer1 = input("Entrer le nom du joueur 1: ")
nameplayer2 = input("Entrer le nom du joueur 2: ")

random = random.randint(1, 2)

if random == 1:
    print(f"{nameplayer1} commence la partie.")
else:
    print(f"{nameplayer2} commence la partie.")
