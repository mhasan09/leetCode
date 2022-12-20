# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        result = 1
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            if not isBadVersion(mid):
                high = mid - 1
                result = mid
            else:
                low = mid + 1

        return result
