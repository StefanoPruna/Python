from tictactoe import *
import unittest

class TicTacToeTest(unittest.TestCase):
    def getFullBoard(self):
        board = [["o", "o", "x"], ["x", "x", "o"], ["o", "x", "x"]]
        return board

    def testInitialiseBoard(self):
        #The board is empty
        board = initialiseBoard()
        self.assertEqual(board, [["0", "1", "2"], ["3", "4", "5"], ["6", "7", "8"]])

    def testEmptySquareAvailable(self):
        #if there is emptied squares
        board = self.getFullBoard()
        board[2][1] = " "
        self.assertTrue(isEmptySquare(board))

    def testEmptySquareNotAvailable(self):
        #Check if the board is full
        board = self.getFullBoard()
        self.assertFalse(isEmptySquare(board))
    
    def winGames(self, player):
        board = self.getFullBoard()
        for row in board:
            row[0] = player
            row[1] = player
            row[2] = player
            self.assertTrue(gameWon(player, board))
            row[0] = " "

    def testGameWon(self):
        self.winGames("o")
        self.winGames("x")

    def testGameNotWon(self):
        board = self.getFullBoard()
        self.assertFalse(gameWon(board,"o"))
        self.assertFalse(gameWon(board, "x"))
        
if __name__ == "__main__":
    unittest.main()

#my initial way
# grid = [["0", "x", " "], [" ", " ", " "], [" ", " ", " "]]
# print(grid)
# player1 = grid[0][1]
# player2 = grid[0][0]
# print(player1, player2)
# gameWon = False
# while(gameWon):
#     for i in grid:
#         if i == grid[" "]:
#             grid[" "] = [player1]
#     else:
#         grid[" "] = player2
# print(grid[i])