from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_left = [i for i in nums if i < pivot]
        pivot_right = [i for i in nums if i > pivot]
        total_element_other_than_pivot = len(pivot_left) + len(pivot_right)
        leftover_elements = len(nums) - total_element_other_than_pivot
        return pivot_left + [pivot for i in range(leftover_elements)] + pivot_right

print(Solution().pivotArray([9,12,5,10,14,3,10], 10)) # [9,5,3,10,10,12,14]
