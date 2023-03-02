import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) <= 1: return nums
            pivot = random.choice(nums)
            less_than, equal_to, greater_than = [], [], []

            for val in nums:
                if val < pivot:
                    less_than.append(val)
                elif val > pivot:
                    greater_than.append(val)
                else:
                    equal_to.append(val)
            return quicksort(less_than) + equal_to + quicksort(greater_than)

        return quicksort(nums)

print(Solution().sortArray([5, 2, 3, 1]))