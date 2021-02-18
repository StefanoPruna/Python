import random

def initialiseBoard():
    return [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]]

def isEmptySquare(board):
    for row in board:
        for square in row:
            if square not in ("x", "o"):
                return True
    return False

def gameWon(player, board):
    for row in board:
        if row[0]==row[1] and row[1]==row[2] and row[0]==player:
            return True          
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i]==board[2][i] and board[0][i]==player:
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0]==player:
        return True
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0]==player:
        return True
    return False


def printBoard(board):
    print("{0} | {1} | {2}".format(board[0][0], board[0][1], board[0][2])) #substitute the cells 0|1|2 with the board index
    print("--------")
    print("{0} | {1} | {2}".format(board[1][0], board[1][1], board[1][2])) #substitute the cells 0|1|2 with the board index
    print("--------")
    print("{0} | {1} | {2}".format(board[2][0], board[2][1], board[2][2])) #substitute the cells 0|1|2 with the board index


def getUserMove(board, player):
    printBoard(board)
    move = None
    while not move:
        move = input("Enter the number of the square you wish to move in: ")
        while not move:
            try:
                move = int(move)
            except ValueError:
                print("It has to be an integer")

        for row in board:
            for i in range(len(row)):
                if row[i] == move:
                    row[i]=player
                    return board

        print("Please enter a valid move")
    return board


def getComputerMove(board, player):
    while isEmptySquare(board):
        i = random.randrange(0, len(board)) 
        j = random.randrange(0, len(board[i]))
        if board[i][j] not in("x", "o"):
            board[i][j]=player
            return board


def main():
    board = initialiseBoard()
    player = "x"
    while not gameWon(board, "x") and not gameWon(board, "o") and isEmptySquare(board):
        if player == "x":
            #get the player to move:
            board = getUserMove(board, player)
        else:
            board = getComputerMove(board, player)

        #switch to other player:
        if player == "x":
            player = "o"
        else:
            player = "x"
    printBoard(board)    
    if gameWon(board, "x"):
        print("X wins!")
    elif gameWon(board, "o"):
        print("O wins!")
    else:
        print("it's a tie")


if __name__=="__main__":
    main()