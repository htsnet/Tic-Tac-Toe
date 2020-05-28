# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:25:04 2020

@author: hamil
"""

import random


player = 0
board = []
sign = ''
computer = 0
start = True


def reset():
    global board
    board = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        ]
    
def printBoard():
    print(board[0], "|" , board[1], "|", board[2])    
    print("-", "|" , "-", "|", "-")
    print(board[3], "|" , board[4], "|", board[5])
    print("-", "|" , "-", "|", "-")
    print(board[6], "|" , board[7], "|", board[8])
    

def choosePosition():
    global board
    while True:
        pos = int(input("Choose one free place: "))
        print("Your choose is {} ".format(pos))
        if pos < 1 or pos > 9:
            print("Invalid number ")
            continue
        if board[pos - 1] == "X" or board[pos - 1] == "O":
            print("Position already played ")
            continue
        break
    return pos
    
    
def markPosition(pos):
    global board
    board[pos-1] = sign   
    printBoard()

    
def checkSituation():
    global board
    result = check([0, 1, 2])
    if result:
        return True
    
    result = check([3, 4, 5])
    if result:
        return True
    
    result = check([6, 7, 8])
    if result:
        return True
    
    result = check([0, 3, 6])
    if result:
        return True
    
    result = check([1, 4, 7])
    if result:
        return True
    
    result = check([2, 5, 8])
    if result:
        return True
    
    result = check([0, 4, 8])
    if result:
        return True
     
    result = check([2, 4, 6])
    if result:
        return True
    #no game over
    return False


def check(list):
    global board
    count = 0
    for x in list:
        if board[x] == sign:
            count = count + 1
    #print(count)   
    if count == 3:
        return True
                
        
def gameOver():
    print("The player {} ({}) win!".format(player, sign))        


def gameDraw():
    global board
    for x in (range(0, 9)):
        if board[x] != "X" or board[x] != "O":
            return False
        else:
            print("The player is draw...")
            return True


#aguarda resposta do número do jogador
while player < 1 or player > 2:
    player = int(input("Choose your player (1 or 2) "))    

    
#jogador inicial escolhido
print("You choose to be the player {} ".format(player))
if player == 1:
    print("Your sign is X")
    sign = "X"
    computer = 2
else: 
    print("Your sign is O")
    sign = "O"
    computer = 1


#computer playing
def computerPlay():
    global board
    freePositions = []
    for x in (range(0, 9)):
        if board[x] == "X" or board[x] == "O":
            pass
        else:
            freePositions.append(x)
    #print(freePositions)        
    pos = random.choice(freePositions)
    print("\nComputer choose {} ".format(pos + 1))
    return pos + 1
            
            
#prepare the game
reset()
printBoard()


#start the game
while True:
    if start == True and player == 2:
        player = 1
        sign = "X"
        pos = computerPlay()
    else:
        if player == computer:
            pos = computerPlay()
        else:
            pos = choosePosition()
    start = False
    markPosition(pos)
    situation = checkSituation()
    if situation == True:
        gameOver()
        break
    else:
        #check if draw
        draw = gameDraw()
        if draw == True:
            break
        else:
            #change player                
            if player == 1:
                player = 2
                sign = "O"
            else:
                player = 1
                sign = "X"
