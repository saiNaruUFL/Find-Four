

#Based on user's inputed row-size and column-size a blank arr size of [rowSize][columnSize]
#is generated and is filled with the character '.'
def get_initial_board(rowSize, columnSize):
    l1 = []
    for rS in range(rowSize):
        l1.append(['.'] * columnSize)
    return l1

#Prints the Board Game in a user friendly fashon. Using "".join at top and bottomn to genereate the top and bottom border(i.e '________" and "-------")
#Middle Logic prints individual row (i.e. "| x o x o x |")
def print_board(boardGame):
    #Printing top border "___________________"
    print(" ",end='')
    print(''.join(['_'] * (len(boardGame[0]) * 2 - 1)))
    
    for row in boardGame:
        print('|',end='')
        print(' '.join(row),end='')
        print('|')

    #Printing bottom border "-----------------"
    print(" ",end='')
    print(''.join(['-'] * (len(boardGame[0]) * 2 - 1)))

#Insers chip based on the user's inputed columna and chip type. Logic fixes the column and loops from bottom-up to an avaiable spot
#If an avaiable spot in that column is found, in other words a '.' is found, then that spot is occupied by the plyers chip type
#Also, used len(boardGame) - row - 1 to return the desired row column basing row index at the bottom of 2d array
def insert_chip(boardGame,column,chip):
    for row in range(len(boardGame)-1,-1,-1):
        #Looping from bottom up on specfic column and looking for empty spot
        if(boardGame[row][column] == '.'):
            boardGame[row][column] = chip
            return len(boardGame) - row - 1

#Based on the given row,column, and chip state, logic has four pointers. The bottom and top pointers move up and down to find
#a vertical consective line until four chips have been found. Same logic applies to horzointal pointers moving left and right

def is_win_state(chip,board,row,column):
  
    #intializign pointers and setting default score(or number of consective chips to 0)
    score = 1
    rowBottomPointer = row + 1
    rowTopPointer = row - 1
    columnPointerLeft = column - 1
    columnPointerRight = column + 1

    if(chip != board[row][column]):
        return False


    #finding consective chips that are to the up of inserted chip
    while(rowTopPointer >= 0 and score < 4 and board[rowTopPointer][column] == chip):
        score += 1
        rowTopPointer -= 1

   #finding consective ships that down of inserted chip
    while(rowBottomPointer < len(board) and score < 4 and board[rowBottomPointer][column] == chip):
        score += 1
        rowBottomPointer += 1

    #If there were four matching consecutvie chips, then this player has won
    if(score >= 4):
        return True

    #score is reset to 1, to find horizontal chips
    score = 1

    #finding consectiuve right chips 
    while(columnPointerRight < len(board[0]) and score < 4 and board[row][columnPointerRight] == chip):
        columnPointerRight += 1
        score += 1

    #finding consecutvie left chips
    while(columnPointerLeft >= 0 and score < 4 and board[row][columnPointerLeft] == chip):
        score += 1
        columnPointerLeft -= 1  

    if(score >= 4):
        return True
    return False

#If all spots on the board game are occipied, then the board is full and returns true, else returns false meaning there is an open spot and the game can
#continue
def is_board_full(boardGame):
    for row in boardGame:
        for element in row:
            if(element == '.'):
                return False

    return True

#The function keeps lrunning until the user inputs valid dimensions of board game.
#If the input size is too small, then a specifc error is outputted and likewise for sizes too big
def getSize(inputStatement1,error1,error2):
    while(True):

        try:
            size1 = int(input(inputStatement1))
            if(size1 < 4):
                print(error1)
            elif(size1 > 25):
                print(error2)
            else:
                return size1
        except ValueError:
            print("Error not a number!")

#Welcome screen prints the the intro screen and receives dimenstiosn for height and width 
def welcomeScreen():
    print("Welcome to Find Four! ")
    print("--------------------- ")

    height = getSize("Enter height of board (rows): ","Error: height must be at least 4!","Error: height can be at most 25!")
    width = getSize("Enter width of board (columns): ","Error: width must be at least 4!","Error: width can be at most 25!")

    return [height,width]

#Before inserting chip at speciifc column, functions checks if the asked column is a valid request
#If it is a valid request, then code checks if column is full. If all cases are checked, then function will return column
def getEntry(inputStatement1,columnLength,boardGame):
    while(True):
        try:
            columnChosen = int(input(inputStatement1))
            if(columnChosen < 0 or columnChosen > columnLength - 1):
                print("Error: no such column!")
            elif(boardGame[0][columnChosen] != '.'):
                print("Error: column is full!")
            else:
                return columnChosen
        except ValueError:
            print("Error: not a number!")

def main():
    #Variable that checks if a player has won, if won the loop breaks
    winState = False
    heightWidth = welcomeScreen()
    boardGame = get_initial_board(heightWidth[0],heightWidth[1])

    player1Chip = 'x'
    player2Chip = 'o'
    
    print_board(boardGame)
    print("Player 1: x")
    print("Player 2: o")

    while(not winState):
        if(is_board_full(boardGame)):

            print("Draw Game! Players tied.")
            return
        player1Column = getEntry("Player 1 - Select Column: ",len(boardGame[0]),boardGame)
        print()
        player1Row =  insert_chip(boardGame,player1Column,player1Chip)
        
        print_board(boardGame)

        if(is_win_state(player1Chip,boardGame,len(boardGame) - player1Row - 1,player1Column)):
            print("Player 1 won the game!")
            return
        if(is_board_full(boardGame)):
            print("Tie! Board is full")

        player2Column = getEntry("Player 2 - Select Column: ",len(boardGame[0]),boardGame)
        print()
        player2Row =  insert_chip(boardGame,player2Column,player2Chip)

        print_board(boardGame)

        if(is_win_state(player2Chip,boardGame,len(boardGame) - player2Row - 1,player2Column)):
            print("Player 2 won the game!")
            return
        
if __name__ == "__main__":
    main()
    

        
