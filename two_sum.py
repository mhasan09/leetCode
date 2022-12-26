from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i


print(Solution().twoSum([2, 7, 11, 15], 9))
# print(Solution().twoSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
