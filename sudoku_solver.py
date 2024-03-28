from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]):
        def is_valid(row:int, col:int, board, number:str):
            for i in range(9):
                if number == board[row][i]:
                    return False
                if number == board[i][col]:
                    return False
                if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)] == number:
                    return False
            return True

        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for n in "123456789":
                            if is_valid(i, j, board, n):
                                board[i][j] = str(n)
                                if solve(board):
                                    return True
                                board[i][j] = "."
                        return False
            return True
        solve(board)



print(Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."],
                              ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                              [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
