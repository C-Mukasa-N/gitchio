#-----------------------------------------------------------------------------------------------
#                                        << Imports >>
#-----------------------------------------------------------------------------------------------
import pgzrun
from random import randint

#-----------------------------------------------------------------------------------------------
#                                       << Variables >>
#-----------------------------------------------------------------------------------------------
WIDTH = 800
HEIGHT = 700

balls = ["ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "ball_6"]
code_generator = []
code = []
code_size = 4
user_ans = []
user_tries = []
essais = 8
try_1 = []
try_2 = []
try_3 = []
try_4 = []
try_5 = []
try_6 = []
try_7 = []
try_8 = []
msg = ""
chosen_balls = []

#-----------------------------------------------------------------------------------------------
#                                        << Objets >>
#-----------------------------------------------------------------------------------------------
# - création code :
for index in range(code_size):
    code_generator.append(balls[randint(0, len(balls) - 1)])

for index in range(code_size):
    ball_code = Actor(code_generator[index])
    ball_code.pos = [(index + 1) * 70, 44]
    code.append(ball_code)

for x in range(code_size): # lignes
    for y in range(essais): # colonnes
        ball = Actor("empty_space")
        ball.pos = [(x + 1) * 70, (y + 2) * 70]
        user_tries.append(ball)

#-----------------------------------------------------------------------------------------------
#                                       << Affichage >>
#-----------------------------------------------------------------------------------------------
def draw():
    global msg
    screen.clear()
    if essais == 0:
        for ball in code:
            ball.draw()
        msg = "DÉFAITE"
        screen.draw.text("Press X to exit", (360, 74), color = "red")
    
    for ball in user_tries:
        ball.draw()
    
    offset = 0
    for ball in chosen_balls:
        ball.pos = [650 + offset, 122]
        ball.draw()
        offset += 40

    screen.draw.text("B = bleu, G = vert, P = mauve,", (550, 10))
    screen.draw.text("R = rouge, W = blanc, Y = jaune", (541, 30))
    screen.draw.text("Choisi 4 couleurs ", (593, 50))
    screen.draw.text("Dernières couleurs choisies: ", (563, 80))
    if msg == "VICTOIRE":
        screen.draw.text(msg, (340, 34), fontsize = 50, color = "blue")
        screen.draw.text("Press X to exit", (365, 74), color = "red")
    else:
        screen.draw.text(msg, (370, 34), fontsize = 30, color = "purple")
    
    if len(try_1) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_1)), (325, 610))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_1)), (325, 630))
    if len(try_2) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_2)), (325, 540))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_2)), (325, 560))
    if len(try_3) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_3)), (325, 470))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_3)), (325, 490))
    if len(try_4) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_4)), (325, 400))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_4)), (325, 420))
    if len(try_5) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_5)), (325, 330))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_5)), (325, 350))
    if len(try_6) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_6)), (325, 260))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_6)), (325, 280))
    if len(try_7) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_7)), (325, 190))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_7)), (325, 210))
    if len(try_8) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_8)), (325, 120))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_8)), (325, 140))
    screen.draw.text("essais restants: " + str(essais), (10, 680))

#-----------------------------------------------------------------------------------------------
#                                       << Evenements >>
#-----------------------------------------------------------------------------------------------
def on_key_down(key):
    global chosen_balls
    
    if len(chosen_balls) == 4:
            chosen_balls = []
    if key == keys.A:
        print(chosen_balls)
        print(user_ans)

    if key == keys.B:
        user_ans.append(balls[0])
        chosen_balls.append(Actor(balls[0]))

    if key == keys.G:
        user_ans.append(balls[1])
        chosen_balls.append(Actor(balls[1]))

    if key == keys.P:
        user_ans.append(balls[2])
        chosen_balls.append(Actor(balls[2]))

    if key == keys.R:
        user_ans.append(balls[3])
        chosen_balls.append(Actor(balls[3]))

    if key == keys.W:
        user_ans.append(balls[4])
        chosen_balls.append(Actor(balls[4]))

    if key == keys.Y:
        user_ans.append(balls[5])
        chosen_balls.append(Actor(balls[5]))

    if key == keys.BACKSPACE:
        chosen_balls.remove(chosen_balls[-1])
        user_ans.remove(user_ans[-1])
    
    if key == keys.X:
        exit()
    
    if len(user_ans) == code_size:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 4:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 8:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 12:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 16:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 20:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 24:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 28:
        check_user_ans(user_ans)

    

#-----------------------------------------------------------------------------------------------
#                                        << Updates >>
#-----------------------------------------------------------------------------------------------
def update():
    pass
#-----------------------------------------------------------------------------------------------
#                                       << Fonctions >>
#-----------------------------------------------------------------------------------------------
def check_user_ans(user_ans):
    if len(user_ans) == code_size:
       for index in range(code_size):
           try_1.append(user_ans[index])
           user_tries[index] = Actor(user_ans[index])
           user_tries[index].pos = [(index + 1) * 70, 630]
       check_victory(try_1)
    
    if len(user_ans) == (code_size + 4):
       for index in range(code_size):
           try_2.append(user_ans[index + 4])
           user_tries[index + 4] = Actor(user_ans[index + 4])
           user_tries[index + 4].pos = [(index + 1) * 70, 560]
       check_victory(try_2)

    if len(user_ans) == (code_size + 8):
       for index in range(code_size):
           try_3.append(user_ans[index + 8])
           user_tries[index + 8] = Actor(user_ans[index + 8])
           user_tries[index + 8].pos = [(index + 1) * 70, 490]
       check_victory(try_3)

    if len(user_ans) == (code_size + 12):
       for index in range(code_size):
           try_4.append(user_ans[index + 12])
           user_tries[index + 12] = Actor(user_ans[index + 12])
           user_tries[index + 12].pos = [(index + 1) * 70, 420]
       check_victory(try_4)

    if len(user_ans) == (code_size + 16):
       for index in range(code_size):
           try_5.append(user_ans[index + 16])
           user_tries[index + 16] = Actor(user_ans[index + 16])
           user_tries[index + 16].pos = [(index + 1) * 70, 350]
       check_victory(try_5)

    if len(user_ans) == (code_size + 20):
       for index in range(code_size):
           try_6.append(user_ans[index + 20])
           user_tries[index + 20] = Actor(user_ans[index + 20])
           user_tries[index + 20].pos = [(index + 1) * 70, 280]
       check_victory(try_6)
    if len(user_ans) == (code_size + 24):
        for index in range(code_size):
           try_7.append(user_ans[index + 24])
           user_tries[index + 24] = Actor(user_ans[index + 24])
           user_tries[index + 24].pos = [(index + 1) * 70, 210]
        check_victory(try_7)

    if len(user_ans) == (code_size + 28):
       for index in range(code_size):
           try_8.append(user_ans[index + 28])
           user_tries[index + 28] = Actor(user_ans[index + 28])
           user_tries[index + 28].pos = [(index + 1) * 70, 140]
       check_victory(try_8)

def check_victory(morceau : list):
    global msg, code_generator, essais
    if morceau == code_generator:
        msg = "VICTOIRE"
    else:
        msg = "RÉESSAYEZ"
        essais = essais - 1

def check_good(morceau : list):
    good_index = []
    for index in range(code_size):
        if morceau[index] == code_generator[index]:
            good_index.append(index)
    return len(good_index)

def check_wrong(morceau : list):
    wrong_index = []
    good_index = []
    for index in range(code_size):
        if morceau[index] == code_generator[index]:
            good_index.append(index)
    for index in range(code_size):
        if morceau[index] != code_generator[index]:
            for j in range(code_size):
                if morceau[index] == code_generator[j] and j not in good_index and j not in wrong_index:
                    wrong_index.append(j)
                    break
    return len(wrong_index)

#-----------------------------------------------------------------------------------------------
#                                      << Run the game >>
#-----------------------------------------------------------------------------------------------
pgzrun.go()#-----------------------------------------------------------------------------------------------
#                                        << Imports >>
#-----------------------------------------------------------------------------------------------
import pgzrun
from random import randint

#-----------------------------------------------------------------------------------------------
#                                       << Variables >>
#-----------------------------------------------------------------------------------------------
WIDTH = 800
HEIGHT = 700

balls = ["ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "ball_6"]
code_generator = []
code = []
code_size = 4
user_ans = []
user_tries = []
essais = 8
try_1 = []
try_2 = []
try_3 = []
try_4 = []
try_5 = []
try_6 = []
try_7 = []
try_8 = []
msg = ""
chosen_balls = []

#-----------------------------------------------------------------------------------------------
#                                        << Objets >>
#-----------------------------------------------------------------------------------------------
# - création code :
for index in range(code_size):
    code_generator.append(balls[randint(0, len(balls) - 1)])

for index in range(code_size):
    ball_code = Actor(code_generator[index])
    ball_code.pos = [(index + 1) * 70, 44]
    code.append(ball_code)

for x in range(code_size): # lignes
    for y in range(essais): # colonnes
        ball = Actor("empty_space")
        ball.pos = [(x + 1) * 70, (y + 2) * 70]
        user_tries.append(ball)

#-----------------------------------------------------------------------------------------------
#                                       << Affichage >>
#-----------------------------------------------------------------------------------------------
def draw():
    global msg
    screen.clear()
    if essais == 0:
        for ball in code:
            ball.draw()
        msg = "DÉFAITE"
        screen.draw.text("Press X to exit", (360, 74), color = "red")
    
    for ball in user_tries:
        ball.draw()
    
    offset = 0
    for ball in chosen_balls:
        ball.pos = [650 + offset, 122]
        ball.draw()
        offset += 40

    screen.draw.text("B = bleu, G = vert, P = mauve,", (550, 10))
    screen.draw.text("R = rouge, W = blanc, Y = jaune", (541, 30))
    screen.draw.text("Choisi 4 couleurs ", (593, 50))
    screen.draw.text("Dernières couleurs choisies: ", (563, 80))
    if msg == "VICTOIRE":
        screen.draw.text(msg, (340, 34), fontsize = 50, color = "blue")
        screen.draw.text("Press X to exit", (365, 74), color = "red")
    else:
        screen.draw.text(msg, (370, 34), fontsize = 30, color = "purple")
    
    if len(try_1) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_1)), (325, 610))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_1)), (325, 630))
    if len(try_2) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_2)), (325, 540))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_2)), (325, 560))
    if len(try_3) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_3)), (325, 470))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_3)), (325, 490))
    if len(try_4) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_4)), (325, 400))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_4)), (325, 420))
    if len(try_5) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_5)), (325, 330))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_5)), (325, 350))
    if len(try_6) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_6)), (325, 260))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_6)), (325, 280))
    if len(try_7) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_7)), (325, 190))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_7)), (325, 210))
    if len(try_8) == code_size:
        screen.draw.text("bonne(s) couleur(s), bien placee(s): " + str(check_good(try_8)), (325, 120))
        screen.draw.text("bonne(s) couleur(s), mal placee(s): " + str(check_wrong(try_8)), (325, 140))
    screen.draw.text("essais restants: " + str(essais), (10, 680))

#-----------------------------------------------------------------------------------------------
#                                       << Evenements >>
#-----------------------------------------------------------------------------------------------
def on_key_down(key):
    global chosen_balls
    
    if len(chosen_balls) == 4:
            chosen_balls = []
    if key == keys.A:
        print(chosen_balls)
        print(user_ans)

    if key == keys.B:
        user_ans.append(balls[0])
        chosen_balls.append(Actor(balls[0]))

    if key == keys.G:
        user_ans.append(balls[1])
        chosen_balls.append(Actor(balls[1]))

    if key == keys.P:
        user_ans.append(balls[2])
        chosen_balls.append(Actor(balls[2]))

    if key == keys.R:
        user_ans.append(balls[3])
        chosen_balls.append(Actor(balls[3]))

    if key == keys.W:
        user_ans.append(balls[4])
        chosen_balls.append(Actor(balls[4]))

    if key == keys.Y:
        user_ans.append(balls[5])
        chosen_balls.append(Actor(balls[5]))

    if key == keys.BACKSPACE:
        chosen_balls.remove(chosen_balls[-1])
        user_ans.remove(user_ans[-1])
    
    if key == keys.X:
        exit()
    
    if len(user_ans) == code_size:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 4:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 8:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 12:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 16:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 20:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 24:
        check_user_ans(user_ans)

    if len(user_ans) == code_size + 28:
        check_user_ans(user_ans)

    

#-----------------------------------------------------------------------------------------------
#                                        << Updates >>
#-----------------------------------------------------------------------------------------------
def update():
    pass
#-----------------------------------------------------------------------------------------------
#                                       << Fonctions >>
#-----------------------------------------------------------------------------------------------
def check_user_ans(user_ans):
    if len(user_ans) == code_size:
       for index in range(code_size):
           try_1.append(user_ans[index])
           user_tries[index] = Actor(user_ans[index])
           user_tries[index].pos = [(index + 1) * 70, 630]
       check_victory(try_1)
    
    if len(user_ans) == (code_size + 4):
       for index in range(code_size):
           try_2.append(user_ans[index + 4])
           user_tries[index + 4] = Actor(user_ans[index + 4])
           user_tries[index + 4].pos = [(index + 1) * 70, 560]
       check_victory(try_2)

    if len(user_ans) == (code_size + 8):
       for index in range(code_size):
           try_3.append(user_ans[index + 8])
           user_tries[index + 8] = Actor(user_ans[index + 8])
           user_tries[index + 8].pos = [(index + 1) * 70, 490]
       check_victory(try_3)

    if len(user_ans) == (code_size + 12):
       for index in range(code_size):
           try_4.append(user_ans[index + 12])
           user_tries[index + 12] = Actor(user_ans[index + 12])
           user_tries[index + 12].pos = [(index + 1) * 70, 420]
       check_victory(try_4)

    if len(user_ans) == (code_size + 16):
       for index in range(code_size):
           try_5.append(user_ans[index + 16])
           user_tries[index + 16] = Actor(user_ans[index + 16])
           user_tries[index + 16].pos = [(index + 1) * 70, 350]
       check_victory(try_5)

    if len(user_ans) == (code_size + 20):
       for index in range(code_size):
           try_6.append(user_ans[index + 20])
           user_tries[index + 20] = Actor(user_ans[index + 20])
           user_tries[index + 20].pos = [(index + 1) * 70, 280]
       check_victory(try_6)
    if len(user_ans) == (code_size + 24):
        for index in range(code_size):
           try_7.append(user_ans[index + 24])
           user_tries[index + 24] = Actor(user_ans[index + 24])
           user_tries[index + 24].pos = [(index + 1) * 70, 210]
        check_victory(try_7)

    if len(user_ans) == (code_size + 28):
       for index in range(code_size):
           try_8.append(user_ans[index + 28])
           user_tries[index + 28] = Actor(user_ans[index + 28])
           user_tries[index + 28].pos = [(index + 1) * 70, 140]
       check_victory(try_8)

def check_victory(morceau : list):
    global msg, code_generator, essais
    if morceau == code_generator:
        msg = "VICTOIRE"
    else:
        msg = "RÉESSAYEZ"
        essais = essais - 1

def check_good(morceau : list):
    good_index = []
    for index in range(code_size):
        if morceau[index] == code_generator[index]:
            good_index.append(index)
    return len(good_index)

def check_wrong(morceau : list):
    wrong_index = []
    good_index = []
    for index in range(code_size):
        if morceau[index] == code_generator[index]:
            good_index.append(index)
    for index in range(code_size):
        if morceau[index] != code_generator[index]:
            for j in range(code_size):
                if morceau[index] == code_generator[j] and j not in good_index and j not in wrong_index:
                    wrong_index.append(j)
                    break
    return len(wrong_index)

#-----------------------------------------------------------------------------------------------
#                                      << Run the game >>
#-----------------------------------------------------------------------------------------------
pgzrun.go()