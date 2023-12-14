from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSum = [sum(row) for row in mat]
        # colSum = [sum(mat[j][i] for j in range(len(mat)))  for i in range(len(mat[0]))]
        colSum = [sum(column) for column in zip(*mat)]
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    count += 1
        return count


print(Solution().numSpecial([[1, 0, 0],
                             [0, 0, 1],
                             [1, 0, 0]]))
print(Solution().numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(Solution().numSpecial([[0, 0],
                             [0, 0],
                             [1, 0]]))
