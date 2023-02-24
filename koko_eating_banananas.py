import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc_time(mid, piles):
            sum = 0
            for i in range(len(piles)):
                sum += math.ceil(piles[i]/mid)
            return sum

        low = 1
        high = max(piles)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            time = calc_time(mid, piles)
            if time <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans



print(Solution().minEatingSpeed([3, 6, 7, 11], 8))
