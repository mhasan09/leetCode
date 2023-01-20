from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining not in data:
                data[nums[i]] = i
            else:
                return [i,data[remaining]]
        return []


print(Solution().twoSum([2, 7, 11, 15], 9))
# print(Solution().twoSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164))
