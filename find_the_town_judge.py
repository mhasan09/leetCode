from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == [] and n == 1:
            return 1
        x1 = [x[1] for x in trust]
        x0 = [x[0] for x in trust]

        for i in range(1, n + 1):
            if i in x1:
                if x1.count(i) == (n - 1):
                    if i not in x0:
                        return i
        return -1

print(Solution().findJudge(3, [[1, 3], [2, 3]]))
# print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))

# print(Solution().findJudge(2, [[1, 3], [2, 3]]))
