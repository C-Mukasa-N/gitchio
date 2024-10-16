# Technical Design Document (TDD) - Puissance3

## 1. Introduction

Ce document décrit la conception technique du jeu **Puissance3**, en expliquant les aspects de la structure du code, les technologies utilisées et les spécifications techniques.

## 2. Langages et Technologies Utilisés

- **Langage** : Python
- **Bibliothèque** : pgzero (pour la gestion graphique et les événements)
- **Fichier d'assistance** : `pgzhelper.py` (contient des fonctions utilitaires pour simplifier le développement)

## 3. Architecture du Code

### Structure des Fichiers

- `/Scripts/`
  - `pgzhelper.py` : Contient les fonctions utilitaires utilisées pour l'affichage graphique et l'interaction du jeu.
  - `puissance_3.py` : Le fichier principal du jeu, contenant la logique du jeu, les règles, et le déroulement du tour par tour.
  - `/images/` : Dossier contenant toutes les images nécessaires pour l'interface du jeu (jetons, grille, etc.).

## 4. Composants du Jeu

- **Initialisation** : Configuration des variables initiales, création de la grille et préparation du jeu.
- **Gestion des événements** : Utilisation de pgzero pour gérer les clics et autres interactions.
- **Logique de Jeu** : Vérification de la victoire, placement des jetons, et bascule des tours entre les joueurs.
- **Rendu graphique** : Dessin de la grille et des jetons sur l'écran en utilisant les fonctions de pgzero.

## 5. Fonctionnalités Techniques

- **Détection de la Victoire** : Le jeu vérifie automatiquement après chaque mouvement si un joueur a aligné trois jetons consécutifs.

## 6. Limitations et Améliorations Futures

- **Limitation actuelle** : Pas d'implémentation de l'intelligence artificielle pour jouer contre l'ordinateur.
- **Améliorations possibles** : 
	- Ajouter un mode contre l'ordinateur.
	- Intégrer des effets sonores et des animations.
	- Gérer les entrées invalides ou les mouvements incorrects afin d'éviter les bugs.

## 7. Dépendances

- **Python 3.x** : Assurez-vous que Python 3 est installé.
- **pgzero** : Bibliothèque Python requise pour exécuter le jeu.

## 8. Instructions d'Installation

1. Installer Python 3.x sur votre machine.
2. Installer pgzero en utilisant la commande suivante : pip install pgzero
3. Exécuter le jeu en lançant le fichier `puissance_3.py`.
