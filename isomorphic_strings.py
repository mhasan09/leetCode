from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = []
        t1 = []
        for i in s:
            s1.append(s.index(i))
        for i in t:
            t1.append(t.index(i))

        if s1 == t1:
            return True
        return False

print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
# print(Solution().isIsomorphic("egg", "add"))


