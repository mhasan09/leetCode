class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return len(s) == i


print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("", "ahbgdc"))
print(Solution().isSubsequence("b", "c"))


