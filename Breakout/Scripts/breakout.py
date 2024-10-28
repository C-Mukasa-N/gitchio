import pgzrun
from random import randint
from pgzhelper import *
import os

# Constantes :
# taille de la fenêtre du jeu (en pixels) :
WIDTH = 800
HEIGHT = 600

# variables :
ball_speed = [4, -4]
bonus_speed = [0, 1]
ball_docked = True
point = 0
vie = 3

# listes bonus :
speed_bonus = []

# Actors :
# - création briques :
all_bricks = []
all_super_bricks = []
# for x in range(8): # lignes
#     for y in range(7): # colonnes
# # RMQ : on peut inverser l'ordre des "for" cela n'est pas grave
#         num = randint(1,5)
#         brick = Actor("glass_" + str(num), anchor = ["left", "top"])
#         if num == 5:
#             brick.scale = 0.04
#         else:
#             brick.scale = 0.1
#         brick.pos = [x * 100, y * 30]
#         all_bricks.append(brick)

for x in range(9): # lignes
    for y in range(8): # colonnes
        num = randint(1,5)
        brick = Actor("glass_" + str(num), anchor = ["left", "top"])
        if num == 5:
            brick.scale = 0.04
        else:
            brick.scale = 0.1
        brick.pos = [x * 100, y * 30]
        all_super_bricks.append(brick)

# - création joueur :
player = Actor("banana_peel")
player.scale = 0.2 # <- changer la taille du player
player.pos = [400, 550]

# - création ball :
ball = Actor("falling_man_1")
ball.scale = 0.3
ball.pos = [player.pos[0], player.pos[1] - 50]

# fonctions du jeu, fonctions qui seront appelée à chaque frame :
def draw():
    global ball_docked
    screen.clear()
    screen.blit("background_2", (0,0))
    player.draw()
    
    for brick in all_bricks:
        brick.draw()
    ball.draw()
    
    for brick in all_super_bricks:
        brick.draw()

    for bonus in speed_bonus:
        bonus.draw()
    screen.draw.text('Vie: ' + str(round(vie)), (20,570), color=(240,0,32), fontsize=30)
    if vie == 0:
        ball_docked = True
        screen.draw.text('VOUS AVEZ PERDU', (110,285), color=(255,0,255), fontsize=90)
    if point == 432:
        ball_docked = True
        screen.draw.text('VOUS AVEZ GAGNE', (110,285), color=(255,0,255), fontsize=90)
    
def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]
    # bloquer le player dans la zone de jeu
    if player.pos[0] <= 75:
        player.pos = (75, player.pos[1])
    elif player.pos[0] >= WIDTH - 75:
        player.pos = (WIDTH - 75, player.pos[1])

def on_mouse_up():
    global ball_docked
    ball_docked = False

def update():
    # - déplacement de la ball :
    ball.pos = [ball.pos[0] + ball_speed[0], ball.pos[1] + ball_speed[1]]
    ball.angle = ball.angle + 1 # <- rotation

    # - checker les bords :
    check_borders()

    # - check collision :
    # -- briques :
    check_bricks_collision()

    # -- player :
    check_player_collision()

    # - balle docker sur le player :
    if ball_docked:
        # si figée, elle suit le player
        ball.pos = [player.pos[0], player.pos[1] - 50]
    else:
        # sinon elle suit la vitesse
        ball.pos = [ball.pos[0] + ball_speed[0], ball.pos[1] + ball_speed[1]]
    
    # bonus :
    move_bonus()

# fonctions "helper", fonctions qui seront appelée dans la fonction "update" :
def check_borders():
    global ball_speed, ball_docked, vie # <- annonce que l'on utilise la variable "ball_speed" du code (globale)
    if ball.pos[0] <= 0 or ball.pos[0] >= WIDTH:
        ball_speed = [ball_speed[0] * -1, ball_speed[1]]
    
    if ball.pos[1] < 0:
        ball_speed = [ball_speed[0], ball_speed[1] * -1]
    elif ball.pos[1] >= HEIGHT:
        ball_docked = True
        vie = vie - 1

def check_bricks_collision():
    global ball_speed, point
    # briques normales :
    for brick in all_bricks:
        if ball.colliderect(brick):
            #sounds.glass_breaking.play()
            point = point + 1
            all_bricks.remove(brick)
            # ajout d'un bonus :
            if randint(1, 2) == 2:
                bonus = Actor("speed_bonus2")
                bonus.scale = 0.07
                bonus.pos = brick.pos[0] + 50, brick.pos[1] + 15
                speed_bonus.append(bonus)

                ball_speed = [ball_speed[0], ball_speed[1] * -1]
                break
    # super-briques :
    for brick in all_super_bricks:
        if ball.colliderect(brick):
            #sounds.glass_breaking.play()
            point = point + 5
            all_super_bricks.remove(brick)
            # ajout d'une brique normale à la place d'une super brique :
            new_brick = Actor("broken_glass_2", anchor = ["left", "top"])
            new_brick.scale = 0.1
            new_brick.pos = brick.pos
            all_bricks.append(new_brick)
            ball_speed = [ball_speed[0], ball_speed[1] * -1]
            break

def check_player_collision():
    global ball_speed
    if ball.colliderect(player):
        #if ball_docked == False:
            #sounds.man_sound.play()
        ball_speed = [ball_speed[0], abs(ball_speed[1]) * -1]

def move_bonus():
    global ball_speed
    for bonus in speed_bonus:
        if bonus.colliderect(player):
            #sounds.laugh.play()
            speed_bonus.remove(bonus)
            ball_speed = ball_speed[0] * 1.5, ball_speed[1] * 1.5
            break
        else:
            bonus.pos = [bonus.pos[0] + bonus_speed[0], bonus.pos[1] + bonus_speed[1]]

os.environ['SDL_VIDEO_CENTERED'] = '1'
# run the game
#sounds.banana_sound.play(-1)
pgzrun.go()