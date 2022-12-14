from typing import List
import itertools


class Solution:
    def pivotIndex(self, arr: List[int]) -> int:
        """
        itertools solution
        """
        s1 = list(itertools.accumulate(arr))
        s2 = list(itertools.accumulate(arr[::-1]))
        s2 = s2[::-1]
        for i in range(len(arr)):
            if s1[i] == s2[i]:
                return i
        return -1

    def pivotIndex_2(self, arr: List[int]) -> int:
        """
        sum solution
        """
        left, right = 0, sum(arr)
        for index, num in enumerate(arr):
            right = right - num
            if left == right:
                return index
            left = left + num
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
print(Solution().pivotIndex([2, 1, -1]))
