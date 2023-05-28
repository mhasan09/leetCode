from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            found = False
            for j in ranges:
                if j[0] <= i <= j[1]:
                    found = True
                    break

            if not found:
                return False
        return True

# print(Solution().isCovered([[1, 2], [3, 4], [5, 6]], 2, 5))
# print(Solution().isCovered([[1,10],[10,20]], 21, 21))
print(Solution().isCovered([[1,1]], 1, 50))
print(Solution().isCovered([[1,1]], 1, 1))
