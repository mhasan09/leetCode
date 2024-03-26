from typing import List


class Solution:
    def is_safe(self, row, col, playground, n):
        # checking upper diagonal
        dup_row = row
        dup_col = col

        while row >= 0 and col >= 0:
            if playground[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # checking left
        row = dup_row
        col = dup_col

        while col >= 0:
            if playground[row][col] == "Q":
                return False
            col -= 1

        # checking lower diagonal
        row = dup_row
        col = dup_col
        while row < n and col >= 0:
            if playground[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True

    def solve(self, col, playground, answer, n):
        if col == n:
            answer.append(["".join(row) for row in playground])
            return

        for row in range(n):
            if self.is_safe(row, col, playground, n):
                # playground[row] = playground[row][:col] + 'Q' + playground[row][col+1:]
                playground[row][col] = 'Q'
                self.solve(col + 1, playground, answer, n)
                playground[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        playground = [["."] * n for _ in range(n)]
        self.solve(0, playground, answer, n)
        return answer


print(Solution().solveNQueens(4))
