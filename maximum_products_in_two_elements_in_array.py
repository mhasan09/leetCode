from typing import List


class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        arr.sort()
        val_1, val_2 = arr[-1], arr[-2]
        return (val_1 - 1) * (val_2 - 1)

print(Solution().maxProduct( [3,4,5,2]))
print(Solution().maxProduct( [1,5,4,5]))