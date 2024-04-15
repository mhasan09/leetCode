from typing import List


class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target > arr[mid]:
                low = mid + 1
            elif target < arr[mid]:
                high = mid - 1
            else:
                return mid
        return low


print(Solution().searchInsert([1, 5, 9, 13, 18, 19, 31, 33, 38], 23))
