from typing import List


class Solution:

    def rob(self, arr):
        if len(arr) == 0:
            return 0

        if len(arr) == 1:
            return arr[0]

        if len(arr) == 2:
            return max(arr[0], arr[1])

        dp = [0] * len(arr)

        dp[0] , dp[1] = arr[0], max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i] = max(dp[i-2] + arr[i], dp[i-1])

        return max(dp)

print(Solution().rob([1, 2, 3, 1]))
