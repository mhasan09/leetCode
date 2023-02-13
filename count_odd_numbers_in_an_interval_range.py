class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


print(Solution().countOdds(3, 7))
print(Solution().countOdds(8, 10))
print(Solution().countOdds(976487647, 989817026))