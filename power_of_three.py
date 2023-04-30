import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        log = math.log10(n) / math.log10(3)
        return int(log) == log


# print(Solution().isPowerOfThree(27))
print(Solution().isPowerOfThree(9))
