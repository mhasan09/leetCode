from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in reversed(range(0, len(matrix) - 1)):
            for j in range(0, len(matrix[0])):
                min_value = min(matrix[i + 1][j], matrix[i + 1][max(j - 1, 0)], matrix[i + 1][min(j + 1, len(matrix[0]) - 1)])
                matrix[i][j] += min_value
        return min(matrix[0])


print(Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(Solution().minFallingPathSum([[-19, 57], [-40, -5]]))
print(Solution().minFallingPathSum([[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))
