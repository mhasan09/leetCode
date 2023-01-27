from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1 for _ in range(len(nums))]
        prefix_sum[0] = 1
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i - 1] * prefix_sum[i - 1]

        postfix_sum = [1 for _ in range(len(nums))]
        postfix_sum[len(nums) - 1] = 1

        for i in range(len(nums) - 2, -1, -1):
            postfix_sum[i] = nums[i+1] * postfix_sum[i+1]

        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = prefix_sum[i] * postfix_sum[i]
        return res




print(Solution().productExceptSelf([1, 2, 3, 4]))
