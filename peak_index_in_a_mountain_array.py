from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low


print(Solution().peakIndexInMountainArray([1,3,3,5,6,4,3,2]))
print(Solution().peakIndexInMountainArray([0,2,1,0]))

