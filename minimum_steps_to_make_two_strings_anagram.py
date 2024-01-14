import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1 = collections.Counter(s)
        t1 = collections.Counter(t)
        val = 0
        for i in s1.keys():
            if i in t1.keys() and s1[i] < t1[i]:
                continue
            elif i in t1.keys() and s1[i] > t1[i]:
                val += s1[i] - t1[i]
            elif i not in t1.keys():
                val += s1[i]
            else:
                continue
        return val


print(Solution().minSteps("leetcode","practice"))
print(Solution().minSteps("bab","aba"))
print(Solution().minSteps("leetcode","practice"))