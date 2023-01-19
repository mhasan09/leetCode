# from typing import List
#
#
# class Solution:
#     @staticmethod
#     def check_divisible(arr, k):
#         counter = 0
#         if sum(arr) % k == 0:
#             counter += 1
#         return counter
#
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         divisible_arr = []
#         for i in range(0, len(nums)):
#             for j in range(i, len(nums)):
#                 divisible_arr.append(self.check_divisible(nums[i:j+1], k))
#         return sum(divisible_arr)
#
#
# print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
# print(Solution().subarraysDivByK([5], 9))
from collections import defaultdict
from typing import List


class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda: 0)
        d[0] = 1
        n = len(nums)
        total = 0
        ans = 0
        for i in range(n):
            total += nums[i]
            ans += d[total % k]
            d[total % k] += 1
        return ans


print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
print(Solution().subarraysDivByK([5], 9))
