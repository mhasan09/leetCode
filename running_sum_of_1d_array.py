import itertools

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = itertools.accumulate(nums)
        return [i for i in result]


print(Solution().runningSum([1, 2, 3, 4]))
