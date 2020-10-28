from os import system
from time import sleep

board=[" "]*10
p1="one"
p2="two"

def display(board):
     system("clear")
     print(board[7]+'|'+board[8]+'|'+board[9])
     print(' ---')
     print(board[4]+'|'+board[5]+'|'+board[6])
     print(' ---')
     print(board[1]+'|'+board[2]+'|'+board[3])

def player_choice():
    is_correct=False
    global p1
    global p2
    while is_correct==False:
        ch=input("Which user wants to take X: ")
        if ch.isdigit()==False:
            print("Enter Digit!")
        elif int(ch) not in [1,2]:
            print("Enter choice from (1/2) it is not in Range")
        else:
            if int(ch)==1:
                p1="X"
                p2="O"
            else:
                 p1="O"
                 p2="X"
            is_correct=True


def user_choice(playernum):
    global p1,p2
    player=""
    if playernum==1:
        player=p1
    else:
        player=p2
    is_correct=False
    while is_correct==False:
        ch=input(f"Choose option User {playernum} wants to play (1-9):  ")
        if ch.isdigit()==False:
            print("Please Enter Digit!")
        elif int(ch) not in range(1,10):
            print("Number not in range of (1-9)")
        # elif board[int(ch)] == player :
        #     print(f"Other Player has already played at that position! Its cheating!")
        # else:
        #     print("You Have played there Already! Dont waste Chances...")
        else:
            ch=int(ch)
            board[ch]=player
            display(board)
            is_correct=True

def check_board(playernum):
    global p1,p2
    print("Checking Board...")
    player=""
    if playernum==1:
        player=p1
    else:
        player=p2
    for index,type in enumerate(board):
        if index in [1,4,7] and type == player:
            print("In Liner 1")
            if board[index+1]==player and board[index+2] == player:
                print(f"Player {playernum} Won ! Congrats")
                return True
            else:
                print("Not Liner 1")
        if index in [1,2,3] and type==player:
            print("In Liner 2")

            if board[index + 3]  == player and board[index + 6] == player:
                print(f"Player {playernum} Won ! Congrats")
                return True
            else:
                print("Not Liner 2")

        if index == 1 and type == player:
            print("In Diagonal 1")

            if board[index + 4] == player and board[index+8] == player:
                print(f"Player {playernum} Won ! Congrats")
                return True
            else:
                print("Not Diagonal 1")

        if index == 3 and type == player:
            print("In Diagonal 2")
            if board[index+2]==player and board[index+2]==player:
                print(f"Player {playernum} Won ! Congrats")
                return True
            else:
                print("Not Diagonal 2")
    return False

def game():
    global p1,p2
    display(board)
    player_choice()
    is_won=False
    times=0
    while is_won==False:
        user_choice(1)
        if check_board(1):
            is_won=True
            break
        user_choice(2)
        if check_board(2):
            is_won=True




game()
