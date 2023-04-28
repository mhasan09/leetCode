class Solution:

    def climbStairs(self, n: int) -> int:
        data = [0 for _ in range(45)]
        def count(x):

            if x == 1:
                return 1
            elif x == 2:
                return 2

            if data[x] != 0:
                return data[x]

            val = count(x - 1) + count(x - 2)
            data[x] = val
            return val
        return count(n)


# print(Solution().climbStairs(6))
# print(Solution().climbStairs(2))
# print(Solution().climbStairs(3))
print(Solution().climbStairs(38))
