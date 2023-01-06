from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = 0
        for i in range(len(costs)):
            if costs[i] <= coins:
                bars += 1
                coins -= costs[i]
        return bars


print(Solution().maxIceCream([1, 3, 2, 4, 1], 7))
print(Solution().maxIceCream([10,6,8,7,7,8], 5))
print(Solution().maxIceCream([1,6,3,1,2,5], 20))
