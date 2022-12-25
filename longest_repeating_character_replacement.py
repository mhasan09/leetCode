class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        data = {}
        result = 0
        for i in range(len(s)):
            data[s[i]] = 1 + data.get(s[i], 0)
            if (i - l + 1) - max(data.values()) > k:
                data[s[l]] -= 1
                l += 1
            result = max(result, i - l + 1)
        return result


print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("ABABBA", 2))
print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("ABBB", 2))
