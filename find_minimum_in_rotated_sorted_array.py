from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            mid = (l+r) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return result


print(Solution().findMin([4,5,6,7,0,1,2]))