from typing import List
import itertools


class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        value = itertools.accumulate(arr)
        left_sum = [i for i in value]
        left_sum.insert(0, 0)
        right_sum = left_sum[::-1]
        for i in range(len(left_sum)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
