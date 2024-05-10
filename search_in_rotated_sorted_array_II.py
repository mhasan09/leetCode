from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return True
            if nums[l] == nums[m]:
                l += 1
                continue
            # check if the value is the left part
            if nums[l] <= nums[m]:
                # check for ascending order
                if nums[l] <= target <= nums[m]:
                    # drag the right part
                    r = m - 1
                else:
                    l = m + 1
            else:
                # again check for ascending order
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False


# print(Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
# print(Solution().search([2, 5, 6, 0, 0, 1, 2], 3))
print(Solution().search([1, 0, 1, 1, 1], 0))
