from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max, current_min = 0, 0
        global_max, global_min = nums[0], nums[0]
        for i in nums:
            current_max = max(current_max + i, i)
            current_min = min(current_min + i, i)
            global_max = max(current_max, global_max)
            global_min = min(current_min, global_min)

        return max(sum(nums) - global_min, global_max) if global_max > 0 else global_max


print(Solution().maxSubarraySumCircular([1, -2, 3, -2]))
print(Solution().maxSubarraySumCircular([5, -3, 5]))
print(Solution().maxSubarraySumCircular([9, -4, -7, 9]))
