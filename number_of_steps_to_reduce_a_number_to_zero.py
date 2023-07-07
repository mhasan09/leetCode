class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.helper(num, 0)

    def helper(self, num, counter):
        if num == 0:
            return counter
        if num % 2 == 0:
            return self.helper(num // 2, counter + 1)
        return self.helper(num - 1, counter + 1)


print(Solution().numberOfSteps(14))
