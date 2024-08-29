from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest_range = 0
        for i in range(1, len(arr) - 1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1
                while r+1 < len(arr) and arr[r] > arr[r+1]:
                    r += 1
                longest_range = max(longest_range, r-l+1)
        return longest_range


print(Solution().longestMountain([2,1,4,7,3,2,5]))