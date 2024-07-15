from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [0 for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    result[i] = prices[i] - prices[j]
                    break
                else:
                    result[i] = prices[i]
        result[-1] = prices[-1]
        return result

print(Solution().finalPrices([8, 4, 6, 2, 3]))
print(Solution().finalPrices([10,22,11,3,12,14,2,1]))
