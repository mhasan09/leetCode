import collections
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_data = collections.defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in board_data:
                        for pos in board_data[board[i][j]]:
                            if (pos[0] == i) or (pos[1] == j) or (pos[0] // 3 == i // 3 and pos[1] // 3 == j // 3):
                                return False
                    board_data[board[i][j]].append((i, j))
        return True


print(Solution().isValidSudoku(
    [[".", ".", "4", ".", ".", ".", "6", "3", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
     [".", ".", ".", "5", "6", ".", ".", ".", "."],
     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
     [".", ".", ".", "7", ".", ".", ".", ".", "."],
     [".", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."]]))

# print(Solution().isValidSudoku(
#     [["5", "3", ".", ".", "7", ".", ".", ".", "."]
#         , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#         , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#         , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#         , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#         , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#         , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#         , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#         , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# ))
