#-----------------------------------------------------------------------------------------------
#                                        << Imports >>
#-----------------------------------------------------------------------------------------------
import pgzrun
from pgzhelper import *

#-----------------------------------------------------------------------------------------------
#                                       << Variables >>
#-----------------------------------------------------------------------------------------------
WIDTH = 800
HEIGHT = 600

column_name = ["A", "B", "C", "D", "E"]
winner = None
current_player = 1
tableau = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
]
x = 0
y = 0
ans_list = []

#-----------------------------------------------------------------------------------------------
#                                        << Objets >>
#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
#                                       << Affichage >>
#-----------------------------------------------------------------------------------------------
def draw():
    screen.clear()
    for index in range(len(column_name)):
        screen.draw.text(column_name[index], ((index + 1) * 67, 440), fontsize = 50, color = "blue")

    screen.draw.text("Joueur 1 -> O", (480, 240), fontsize = 50, color = "purple")
    screen.draw.text("Joueur 2 -> X", (480, 275), fontsize = 50, color = "purple")
    screen.draw.text("Joueur " + str(current_player) + " est en train de jouer", (210, 540), fontsize = 40, color = "red")

    for coin in ans_list:
        coin.scale = 0.15
        coin.draw()

    if winner == 1 or winner == 2:
        screen.draw.text("Winner is Joueur " + str(winner), (340, 34), fontsize = 50, color = "blue")
        screen.draw.text("Press X to exit", (365, 74), color = "red")
#-----------------------------------------------------------------------------------------------
#                                       << Evenements >>
#-----------------------------------------------------------------------------------------------
def on_key_down(key):
    global winner, tableau, current_player, x, y

    if current_player == 1:
        jeton = "o"
    else:
        jeton = "x"

    if key == keys.A:
        column = 0
        x = 70
    elif key == keys.B:
        column = 1
        x = 140
    elif key == keys.C:
        column = 2
        x = 210
    elif key == keys.D:
        column = 3
        x = 280
    elif key == keys.E:
        column = 4
        x = 350
    elif key == keys.X:
        exit()
    else:
        return

    tableau = play(tableau, current_player, column)
    if check_winner(tableau, current_player, column):
        winner = current_player
    else:
        current_player = 2 if current_player == 1 else 1

    last_coin = check_last_coin(tableau, column)
    y = 140 + last_coin * 70

    coin = Actor(jeton)
    coin.pos = x, y
    ans_list.append(coin)

#-----------------------------------------------------------------------------------------------
#                                        << Updates >>
#-----------------------------------------------------------------------------------------------
def update():
    pass

#-----------------------------------------------------------------------------------------------
#                                       << Fonctions >>
#-----------------------------------------------------------------------------------------------
def check_last_coin(tableau, column):
    line = len(tableau) - 1
    while tableau[line][column] != ".":
            line = line - 1
    last_line = line
    return last_line

def check_vertical(grid, line, column, jeton):
    if line > 2:
        return False
    
    if grid[line + 1][column] == jeton and grid[line + 2][column] == jeton:
        return True
    
    return False

def check_horizontal(grid, line, column, jeton):
    if column <= 2:
        if grid[line][column + 1] == jeton and grid[line][column + 2] == jeton:
            return True
    
    if column >= 2:
        if grid[line][column - 1] == jeton and grid[line][column - 2] == jeton:
            return True
    
    if column >= 1 and column <= 3:
        if grid[line][column - 1] == jeton and grid[line][column + 1] == jeton:
            return True
    
    return False

def check_diagonale(grid, line, column, jeton):
    # descendant :
    if line <= 2 and column <= 2:
        if grid[line + 1][column + 1] == jeton and grid[line + 2][column + 2] == jeton:
            return True

    if  line >= 2 and column >= 2:  
        if grid[line - 1][column - 1] == jeton and grid[line - 2][column - 2] == jeton:
            return True
    
    if 1 <= line <= 3 and 1 <= column <= 3:
        if grid[line - 1][column - 1] == jeton and grid[line + 1][column + 1] == jeton:
            return True
    
    # montant :
    if line >= 2 and column <= 2:
        if grid[line - 1][column + 1] == jeton and grid[line - 2][column + 2] == jeton:
            return True

    if  line <= 2 and column >= 2:  
        if grid[line + 1][column - 1] == jeton and grid[line + 2][column - 2] == jeton:
            return True
    
    if 1 <= line <= 3 and 1 <= column <= 3:
        if grid[line - 1][column + 1] == jeton and grid[line + 1][column - 1] == jeton:
            return True
        
    return False

def check_winner(grid, player, column):
    # trouver la ligne :
    line = 0
    while grid[line][column] == ".":
        line = line + 1
    
    if player == 1:
        jeton = "O"
    if player == 2:
        jeton = "X"
    
    if check_vertical(grid, line, column, jeton):
        return True
    
    if check_horizontal(grid, line, column, jeton):
        return True

    if check_diagonale(grid, line, column, jeton):
        return True

def play(grid, player, position):
    if player == 1:
        jeton = "O"
    if player == 2:
        jeton = "X"

    line = len(grid) - 1
    while grid[line][position] != ".":
            line = line - 1

    grid[line][position] = jeton
    return grid

#-----------------------------------------------------------------------------------------------
#                                      << Run the game >>
#-----------------------------------------------------------------------------------------------
pgzrun.go()