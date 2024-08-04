from typing import List


class Solution:
    def is_subset_sum(self, arr, n, target):
        data = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            data[i][0] = True

        for i in range(1, target + 1):
            data[0][i] = False

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j < arr[i - 1]:
                    data[i][j] = data[i - 1][j]
                else:
                    data[i][j] = data[i - 1][j] or data[i - 1][j - arr[i - 1]]

        return data[n][target]

    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        return self.is_subset_sum(nums, len(nums), target)


print(Solution().canPartition([1, 5, 11, 5]))
print(Solution().canPartition([1, 2, 5]))
