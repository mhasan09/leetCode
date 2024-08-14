from typing import List


class Solution:
    def rob(self, arr):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]

        prev2 = arr[0]
        prev1 = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            current = max(arr[i] + prev2, prev1)
            prev2 = prev1
            prev1 = current


        return prev1


print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([13, 9, 1, 63, 3, 4]))
