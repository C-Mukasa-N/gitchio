# Game Design Document (GDD) - Puissance3

## 1. Introduction

**Puissance3** est un jeu développé comme un défi personnel après un exercice de ma formation, où nous devions créer un Puissance 3 en Python.
J'ai utilisé pgzero pour combiner les connaissances acquises lors de deux exercices différents.

## 2. Concept du Jeu

- **Genre** : Jeu de puzzle / réflexion
- **Plateforme** : PC (exécutable avec Python et pgzero)
- **Public Cible** : Tous âges, amateurs de jeux de stratégie et de réflexion

## 3. Objectifs du Jeu

L'objectif principal du jeu est de placer trois jetons consécutifs de la même couleur horizontalement, verticalement ou en diagonale pour gagner.

## 4. Mécaniques de Jeu

- **Tour par tour** : Les joueurs placent un jeton à tour de rôle.
- **Vérification de victoire** : Après chaque tour, le jeu vérifie si un joueur a aligné trois jetons.
- **Fin du Jeu** : La partie se termine lorsqu'un joueur a aligné trois jetons.

## 5. Contrôles

- Les contrôles se font avec les touches A, B, C, D et E (les noms des colonnes où placer les jetons).

## 6. Interface Utilisateur

- **Grille de jeu** : La grille affiche les emplacements où les jetons peuvent être placés.
- **Indicateur de tour** : Un indicateur visuel montre à qui c'est le tour de jouer.
- **Message de victoire** : Un message s'affiche lorsque l'un des joueurs gagne la partie.

## 7. Ressources Visuelles et Audio

- **Images** : Des graphiques simples pour les jetons et la grille du jeu.
- **Audio** : Aucun son spécifique prévu pour le moment.

## 8. Inspirations

Ce jeu est inspiré des classiques jeux de stratégie de type "Puissance 3" et "Tic-tac-toe".

