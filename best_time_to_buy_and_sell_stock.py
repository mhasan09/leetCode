from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                current_profit = prices[r] - prices[l]
                max_profit = max(current_profit, max_profit)

            else:
                l = r
            r += 1
        return max_profit


print(Solution().maxProfit([7,1,5,3,6,4]))
# print(Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))
# print(Solution().maxProfit([7, 6, 4, 3, 1]))
