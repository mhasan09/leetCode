from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1) # ["inf", "inf" ....]
        dp[0] = 0 # for amount 0 it will be 0
        for i in range(1, amount + 1): # iterate each amount
            for coin in coins: # iterate each coin
                if i - coin >= 0: # 5(amount) - 2(coin) = 3
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else - 1


print(Solution().coinChange([1, 2, 5], 11))
# print(Solution().coinChange([2, 3, 6, 7], 16))
