import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)

        for i in t_counter:
            if i in s_counter and s_counter[i] == t_counter[i]:
                pass
            else:
                return i


# print(Solution().findTheDifference("abcd", "abcde"))
print(Solution().findTheDifference("abcdff", "abcdfxf"))
print(Solution().findTheDifference("", "y"))
print(Solution().findTheDifference("a", "aa"))
