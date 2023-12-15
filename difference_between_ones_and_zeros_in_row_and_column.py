import collections

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        result_matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
        row_one = []
        row_zero = []

        col_one = []
        col_zero = []

        for row in range(len(grid)):
            data = collections.Counter(grid[row])
            row_one.append(data[1])
            row_zero.append(data[0])

        transposed_mat = [list(row) for row in zip(*grid)]

        for col in transposed_mat:
            data = collections.Counter(col)
            col_one.append(data[1])
            col_zero.append(data[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result_matrix[i][j] = row_one[i] + col_one[j] - row_zero[i] - col_zero[j]

        return result_matrix


print(Solution().onesMinusZeros([[0, 1, 1], [1, 0, 1], [0, 0, 1]]))
