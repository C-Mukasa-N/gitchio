# Technical Design Document (TDD) - Mastermind

## 1. Introduction

Ce document décrit la conception technique du jeu Mastermind, en expliquant les aspects de la structure du code, les technologies utilisées et les spécifications techniques. Ce jeu est développé comme un exercice, tout comme Puissance3, et repose sur des mécanismes de puzzle et de réflexion.

## 2. Langages et Technologies Utilisés

- **Langage** : Python
- **Bibliothèque** : pgzero (pour la gestion graphique et les événements)
- **Fichier d'assistance** : pgzhelper.py (utilisé pour simplifier certaines interactions et l'affichage)

## 3. Architecture du Code

### Structure des Fichiers

- `/Scripts/`
  - `pgzhelper.py` : Contient les fonctions utilitaires utilisées pour l'affichage graphique et l'interaction du jeu.
  - `mastermind.py` : Le fichier principal contenant la logique du jeu, les règles, et la gestion des essais du joueur.

## 4. Composants du Jeu

- **Initialisation** : Configuration des variables de départ, génération aléatoire du code couleur à deviner, et affichage de la grille de jeu.
- **Gestion des événements** : Utilisation de pgzero pour capturer les touches correspondant aux couleurs (B, G, P, R, W, Y) pour que le joueur puisse entrer ses choix.
- **Logique de Jeu** : 
	- Comparaison du code couleur proposé par le joueur avec le code généré.
	- Feedback donné au joueur : couleurs bien placées, mal placées ou incorrectes.
	- Gestion des 8 essais disponibles avant la fin du jeu.
- **Rendu graphique** : Affichage des couleurs choisies, des indices de positionnement, et du code caché.


## 5. Fonctionnalités Techniques

- **Vérification des tentatives** : Après chaque tentative du joueur, le jeu vérifie combien de couleurs sont correctes et bien placées ou mal placées.
- **Gestion des essais** : Le joueur dispose de 8 essais pour deviner le code couleur, après quoi la partie se termine.
- **Affichage dynamique** : Affichage des tentatives et des résultats intermédiaires à chaque essai.

## 6. Limitations et Améliorations Futures

- **Limitation actuelle** : Pas d'option pour ajuster la difficulté (nombre de couleurs, essais supplémentaires, etc.).
- **Améliorations possibles** :
	- Ajouter des niveaux de difficulté (plus de couleurs, moins d'essais).
	- Implémenter des effets visuels plus dynamiques ou des animations lors de la validation d'un essai.
	- Enregistrer le score du joueur ou proposer un mode multijoueur.
	- Ajouter des effets sonores pour les différentes actions du jeu.

## 7. Dépendances

- **Python 3.x** : Assurez-vous que Python 3 est installé.
- **pgzero** : Bibliothèque Python requise pour l'exécution graphique.
- **pgzhelper** : Fichier utilitaire pour simplifier l'affichage et la gestion des événements dans le jeu.

## 8. Instructions d'Installation

1. Installer Python 3.x sur votre machine.
2. Installer pgzero en utilisant la commande suivante : pip install pgzero
3. Exécuter le jeu en lançant le fichier `puissance_3.py`.
