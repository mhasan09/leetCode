from typing import List


class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        res = [1] * len(arr)
        for i in reversed(range(len(arr))):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    res[i] = max(1 + res[j], res[i])
        return max(res)


# print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
# print(Solution().lengthOfLIS([5, 8, 7, 1, 9]))  # 3
print(Solution().lengthOfLIS([1, 2, 4, 3]))  # 3

