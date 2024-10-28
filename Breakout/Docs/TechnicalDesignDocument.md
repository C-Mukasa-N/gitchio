# Technical Design Document (TDD) - Breakout

## 1. Introduction

Ce document décrit la conception technique du jeu Breakout, développé dans le cadre d'un exercice d'introduction à pgzero. Le jeu repose sur une mécanique de destruction d'objets dans un magasin de verres, où le joueur incarne une banane maléfique qui provoque des destructions tout en collectant des bonus. Ce document détaille la structure du code, les technologies utilisées et les spécifications techniques.

## 2. Langages et Technologies Utilisés

- **Langage** : Python
- **Bibliothèque** : pgzero (pour la gestion graphique et les événements)
- **Fichier d'assistance** : pgzhelper.py (utilisé pour simplifier certaines interactions et l'affichage)

## 3. Architecture du Code

### Structure des Fichiers

- `/Scripts/`
  - `pgzhelper.py` : Contient les fonctions utilitaires utilisées pour l'affichage graphique et l'interaction du jeu.
  - `breakout.py` : Le fichier principal contenant la logique du jeu, la gestion des événements et le comportement de la banane maléfique.

## 4. Composants du Jeu

- **Initialisation** : 
	- Configuration des variables de départ, initialisation du personnage (glissant sur la banane maléfique) et des objets destructibles (les verres).
	- Affichage de l'interface de jeu et des compteurs (vies, score).
- **Gestion des événements** : 
	- Utilisation de pgzero pour capturer les interactions de la souris.
	-Clic gauche pour lancer le personnage sur la banane et commencer la destruction des verres.
- **Logique de Jeu** : 
	- Gestion des collisions entre la banane et les objets destructibles.
	- Suivi des bonus (qui accélèrent le personnage et rendent le jeu plus difficile).
	- Suivi des vies et gestion de la fin de partie (victoire ou défaite).
- **Rendu graphique** : 
	- Affichage des verres, du personnage, des bonus et du score.
	- Mise à jour visuelle à chaque événement, comme la destruction des verres et l'apparition des bonus.

## 5. Fonctionnalités Techniques

- **Gestion des collisions** : Chaque collision entre le personnage et les objets destructibles peut entraîner l'apparition de bonus.
- **Gestion des bonus** : Des bonus apparaissent après la destruction de certains verres, augmentant la vitesse du personnage.
- **Suivi des vies** : Le joueur dispose de 3 vies. Une vie est perdue si le joueur ne réussit pas à faire glisser le personnage sur la banane, sortant ce dernier de l'écran.

## 6. Limitations et Améliorations Futures

- **Limitation actuelle** : Le jeu ne dispose pas encore d'animations avancées pour les collisions ou les bonus, ni d'options de difficulté.
- **Améliorations possibles** :
	- Ajouter des niveaux de difficulté (plus de verres, vitesse accrue, moins de vies).
	- Implémenter des effets visuels et des animations lors des collisions ou de la collecte de bonus.
	- Ajouter des effets sonores pour les actions (verres cassés, bonus collectés, etc.).


## 7. Dépendances

- **Python 3.x** : Assurez-vous que Python 3 est installé.
- **pgzero** : Bibliothèque Python nécessaire pour l'exécution du jeu.
- **pgzhelper** : Fichier utilitaire pour simplifier l'affichage et la gestion des événements dans le jeu.

## 8. Instructions d'Installation

1. Installer Python 3.x sur votre machine.
2. Installer pgzero en utilisant la commande suivante : pip install pgzero
3. Exécuter le jeu en lançant le fichier `breakout.py`.
