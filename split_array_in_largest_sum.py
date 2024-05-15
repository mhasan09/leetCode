from typing import List


class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        start, end = max(arr), sum(arr)
        while start <= end:
            mid = start + (end - start) // 2
            total_sum = 0
            part = 1
            for i in arr:
                total_sum += i
                if total_sum <= mid:
                    continue
                else:
                    total_sum = i
                    part += 1
            if part > k:
                start = mid + 1
            else:
                end = mid - 1
        return start



print(Solution().splitArray([7, 2, 5, 10, 8], 2))
