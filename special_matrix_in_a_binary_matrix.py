from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special_position = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    pass
        return special_position


print(Solution().numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(Solution().numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
