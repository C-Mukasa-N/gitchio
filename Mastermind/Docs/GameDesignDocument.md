# Game Design Document (GDD) - Mastermind

## 1. Introduction

**Mastermind** est un jeu de puzzle conçu dans le cadre d'un exercice personnel similaire au projet Puissance3. Le jeu est une version numérique du classique Mastermind, où le joueur doit deviner un code couleur en un nombre limité d'essais.


## 2. Concept du Jeu

- **Genre** : Jeu de puzzle / réflexion
- **Plateforme** : PC (exécutable avec Python et pgzero)
- **Public Cible** : Tous âges, amateurs de jeux de stratégie et de réflexion

## 3. Objectifs du Jeu

L'objectif principal est de deviner une combinaison de quatre couleurs en un maximum de 8 essais. Le joueur reçoit des indices après chaque tentative pour savoir si les couleurs choisies sont correctes et si elles sont bien ou mal placées.

## 4. Mécaniques de Jeu

- **Choix des couleurs** : Le joueur sélectionne quatre couleurs à chaque tour parmi les options disponibles.
- **Vérification des couleurs** : Après chaque tentative, des indices sont donnés pour indiquer :
Si une couleur est correcte et bien placée.
Si une couleur est correcte mais mal placée.
- **Limite d'essais** : Le joueur a 8 tentatives pour deviner la combinaison correcte.
- **Fin du Jeu** : La partie se termine lorsque le joueur trouve la combinaison correcte ou lorsqu'il atteint la limite d'essais.

## 5. Contrôles

Les couleurs sont sélectionnées à l'aide des touches suivantes :
- B = Bleu
- G = Vert
- P = Mauve
- R = Rouge
- W = Blanc
- Y = Jaune

## 6. Interface Utilisateur

- **Grille de jeu** : Une grille affiche les choix du joueur et les indices correspondants pour chaque tentative.
- **Indicateur d'essais restants** : Un compteur affiche le nombre d'essais restants.
- **Message de victoire/défaite** : Un message s'affiche lorsque le joueur devine correctement la combinaison ou lorsqu'il atteint la limite d'essais.

## 7. Ressources Visuelles et Audio

- **Images** : Simples représentations des couleurs pour les balles et les indices.
- **Audio** : Aucun son spécifique prévu pour le moment.

## 8. Inspirations

Ce jeu est inspiré de la version classique du jeu de société "Mastermind", adapté en format numérique pour un exercice de réflexion.
