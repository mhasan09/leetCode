from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero , one = 0, 0
        result = 0
        data = {}
        for index, number in enumerate(nums):
            if number == 0:
                zero += 1
            if number == 1:
                one += 1

            if one - zero not in data:
                data[one - zero] = index

            if one == zero:
                result = one + zero
            else:
                idx = data[one - zero]
                result = max(result, index - idx)
        return result



print(Solution().findMaxLength([1,0,1,1,0]))
