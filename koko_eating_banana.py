import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = math.ceil(sum(piles) / h)
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            total_time = 0
            for i in piles:
                total_time += math.ceil(i / mid)
                if total_time > h:
                    break
            if total_time <= h:
                right = mid
            else:
                left = mid + 1
        return right


print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
