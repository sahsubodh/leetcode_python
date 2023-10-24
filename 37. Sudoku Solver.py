'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self,board):
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j] == "."):
                
                    for c in range(1,10):
                        c = str(c)
                        if (self.is_valid(board,i,j,c)):
                            board[i][j] = c
                        
                            if (self.solve(board) == True):
                                return True
                            else:
                                board[i][j] = "."
                        
                    return False
        return True
    def is_valid(self,board,row,col,c):
        for i in range(0,9):
            if (board[i][col] == c):
                return False
            if (board[row][i] == c):
                return False
            if (board[3*(row//3) + i//3][3*(col//3)+i%3] == c):
                return False
        return True