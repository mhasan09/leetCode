from typing import List


class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        first = self.search(arr,target,False)
        second = self.search(arr,target, True)
        return [first, second]

    def search(self, arr, target, has_found_first_index):
        ans = -1
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                ans = mid
                if has_found_first_index is False:
                    high = mid - 1
                else:
                    low = mid + 1
        return ans





print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
