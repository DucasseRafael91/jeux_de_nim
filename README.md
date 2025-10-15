 Jeux de Nim 

Un jeu classique revisité en Python : deux joueurs s'affrontent pour ne pas ramasser la dernière allumette ! Ce projet inclut deux variantes du jeu :

Variante simple : 1 seul tas de 21 allumettes.

Variante Marienbad : 4 tas (1, 3, 5, 7 allumettes).

📜 Règles du jeu

Variante simple

Le jeu commence avec 21 allumettes.

Chaque joueur, à son tour, retire entre 1 et 4 allumettes.

Le joueur qui retire la dernière allumette perd.

Variante Marienbad 

Il y a 4 tas de tailles différentes : 1, 3, 5, 7 allumettes.

À chaque tour, un joueur choisit un seul tas et y retire au moins une allumette.

Le joueur qui retire la dernière allumette perd.

🤖 Mode contre l'ordinateur

Variante simple

L'ordinateur peut jouer contre vous selon une stratégie gagnante :

Si vous commencez, l'ordinateur répond en retirant 5 - k allumettes, où k est le nombre que vous avez retiré. Cela vous force à finir sur la dernière allumette.

Si l'ordinateur commence, il tente de se ramener à cette situation gagnante en chosissant un nombre aléatoire entre 1 et 4.

Variante Marienbad

Dans cette version, l'ordinateur applique une stratégie simple qui est de choisir aléatoirement un nombre entre 1 et 4.

🕹️ Utilisation

Exécution du jeu
Lancez le script Python depuis votre terminal :

python nim_games.py


Choix du mode

Joueur contre joueur

Joueur contre ordinateur

Variante simple ou Marienbad

Entrée des noms des joueurs

Le jeu demande les noms au démarrage, ainsi que qui commence la partie.

Tour par tour

Chaque joueur indique le nombre d’allumettes à retirer (et le tas, si Marienbad).

📂 Structure du projet
allumettes/
│
├── allumettes.py        # Code principal du jeu
├── README.md            # Ce fichier

✅ Fonctionnalités

Interface console simple et interactive

Prise en compte des erreurs de saisie (valeurs invalides, dépassement de nombre d'allumettes, etc.)

Stratégie gagnante en mode ordinateur (variante simple)

Variante Marienbad avec IA de base

🛠️ Pré-requis

Python 3.x

Aucune bibliothèque externe n’est requise

🚀 Améliorations possibles

Interface graphique (Tkinter ou PyGame)

IA plus intelligente pour Marienbad (algorithme de Nim)

Mode multijoueur en ligne

👨‍💻 Auteurs

Projet éducatif Python

Inspiré du jeu de société Marienbad
