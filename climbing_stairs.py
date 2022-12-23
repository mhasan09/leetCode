class Solution:

    def climbStairs(self, n: int) -> int:
        data = [0 for i in range(45)]

        def stair_climb(x):
            if x == 1:
                return 1
            elif x == 2:
                return 2

            if data[x] != 0:
                return data[x]

            result = stair_climb(x - 1) + stair_climb(x - 2)
            data[x] = result
            return result

        return stair_climb(n)


# print(Solution().climbStairs(6))
# print(Solution().climbStairs(2))
# print(Solution().climbStairs(3))
print(Solution().climbStairs(38))
