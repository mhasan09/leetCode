class Solution:
    def minimumPlatform(self, n, start, dep):
        start.sort()
        dep.sort()
        i, j = 1, 0
        count = 1
        ans = 1
        while i < n and j < n:
            if start[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(ans, count)
        return ans



print(Solution().minimumPlatform(6, [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
# print(Solution().minimumPlatform(3, [900, 1100, 1235], [1000, 1200, 1240]))
