# Game Design Document (GDD) - Breakout

## 1. Introduction

**Breakout** est un jeu de puzzle-action conçu dans le cadre de ma formation, introduisant l'utilisation de la bibliothèque pgzero. Le jeu met en scène un personnage qui glisse sur une banane maléfique dans un magasin de verres, causant un maximum de destructions. Il s'agit d'un exercice axé sur la manipulation de la physique et la gestion des événements avec la souris.


## 2. Concept du Jeu

- **Genre** : Jeu de puzzle / action
- **Plateforme** : PC (exécutable avec Python et pgzero)
- **Public Cible** : Tous âges, amateurs de jeux d'action décalés et de destruction.

## 3. Objectifs du Jeu

Le but du jeu est de faire glisser le personnage sur la banane maléfique pour casser le plus de verres possible dans le magasin. Plus de verres sont détruits, plus il y a de chances de faire tomber des bonus qui accélèrent la vitesse du personnage, rendant ainsi le jeu plus difficile. Le joueur dispose de 3 vies pour réaliser son objectif.

## 4. Mécaniques de Jeu

- **Glissement de la banane** : Le joueur clique avec la souris pour lancer le personnage et le faire glisser sur la banane.
- **Casser les verres** : Lorsque le personnage touche des objets, il détruit les verres du magasin.
- **Collecte de bonus** : Certains verres détruits font tomber des bonus qui augmentent la vitesse du personnage, ajoutant de la difficulté.
- **Gestion des vies** : Le joueur dispose de 3 vies. Si toutes les vies sont perdues, le jeu se termine.
- **Fin du Jeu** :
	- Le joueur gagne s'il détruit tout les verres.
	- Le joueur perd s'il ne parvient pas à détruire suffisamment de verres avant de perdre ses 3 vies.

## 5. Contrôles

Le jeu se joue entièrement à la souris :
Clic gauche : Lance le personnage sur la banane maléfique.

## 6. Interface Utilisateur

- **Grille de jeu** : Une interface simple représentant le magasin, les verres et le personnage.
- **Indicateur de vies** : Le nombre de vies restantes est affiché à l'écran.
- **Messages de victoire ou défaite** : Un message apparaît à l'écran pour indiquer si le joueur a gagné ou perdu.

## 7. Ressources Visuelles et Audio

- **Images** : Représentations du personnage, de la banane maléfique, des verres et des bonus.
- **Audio** : Aucun son spécifique prévu pour le moment.

## 8. Inspirations

Le jeu est inspiré des classiques du genre Breakout, avec une touche d'humour et une mécanique de glissement contrôlée à la souris, rendant le jeu amusant et décalé.
