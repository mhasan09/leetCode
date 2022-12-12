class Solution:

    def climbStairs(self, n: int) -> int:
        data = [0 for i in range(50)]

        def count_stairs(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            elif n == 2:
                return 2

            if data[n] != 0:
                return data[n]
            value = count_stairs(n - 1) + count_stairs(n - 2)
            data[n] = value
            return value
        return count_stairs(n)


print(Solution().climbStairs(6))
