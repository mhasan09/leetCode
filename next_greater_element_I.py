from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater_data = {}
        for num in nums2:
            while len(stack) != 0 and stack[-1] < num:
                next_greater_data[stack.pop()] = num
            stack.append(num)
        result = []
        for num in nums1:
            if num in next_greater_data:
                result.append(next_greater_data[num])
            else:
                result.append(-1)
        return result



print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))