from typing import List, Any


class Solution:
    def check_negative(self, arr):
        for i in arr:
            if i < 0:
                return i
        return 0

    def negativeIntegerInEveryWindow(self, nums: List[int], k: int) -> list[Any]:
        value = []
        for i in range(len(nums)):
            if i + k < len(nums) + 1:
                value.append(self.check_negative(nums[i:i + k]))
        return value


print(Solution().negativeIntegerInEveryWindow([-8, 2, 3, -6, 10], 2))
print(Solution().negativeIntegerInEveryWindow([12, -1, -7, 8, -15, 30, 16, 28], 3))
