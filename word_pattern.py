class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        data = {}
        s = s.split()
        if len(s) != len(pattern) or len(set(pattern)) != len(set(s)):
            return False
        for i, j in zip(pattern, s):
            if i not in data:
                data[i] = j
            else:
                if data[i] != j:
                    return False
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
