"""
Tic-Tac-Toe is game where two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. 
The game is designed in such a way that the player enters a number between [1-9] and the game board will be displayed on screen. At the end of the game system will display the winner.

Game rules:
1. Player 1 plays for [X] --- Player 2 plays for [O]
2. Player enters the number between [1-9] to mark their position
3. If X succeeds in placing three of their marks in a row (up, down, across, or diagonally), then X is the winner.
4. If O succeeds in placing three of their marks in a row (up, down, across, or diagonally), then O is the winner.
5. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

Conditions:
1. You cannot enter the number apart from [1-9] to mark the position. System displays "Please enter the position between [1-9]" message.
2. You cannot fill the position which has already been filled. System displays "Position has been marked already" message.
"""

# Runtime : Python 3.6

import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################    
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")
    print("\n")
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False
    
def playersChance():   
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'
    return Mark
   
#This Function Checks player has won or not    
def CheckWin():
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running
        
        
print("Welcome to Tic-Tac-Toe")
print("Player 1 plays for [X] --- Player 2 plays for [O]\n")
    
 
while(Game == Running):
    DrawBoard() 
    Mark = playersChance()
    choice = int(input("Enter the position between [1-9] where you want to mark : "))
    if(choice != 0 and choice <= 9):
        if(CheckPosition(choice)):
            board[choice] = Mark    
            player+=1    
            CheckWin()
        else:
            print("\n")
            print("Position has been marked already")
            print("\n")
    else:
        print("\n")
        print("Please enter the position between [1-9]")
        print("\n")
  
DrawBoard()    
if(Game==Draw):    
    print("Its a Tie")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Congratulations!! Player 1 Won")    
    else:    
        print("Congratulations!! Player 2 Won")    
