from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x, y = stones[-2], stones[-1]
            stones = stones[:-2]
            if y != x:
                stones.append(y-x)
        return stones[0] if len(stones) else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
