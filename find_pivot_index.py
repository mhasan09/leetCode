from typing import List
import itertools


class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        left, right = 0, sum(arr)
        for index, num in enumerate(arr):
            right = right - num
            if left == right:
                return index
            left = left + num
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([2, 1, -1]))
