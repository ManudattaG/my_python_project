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
