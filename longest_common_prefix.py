class Solution:
    def longest_common_prefix(self, strs):
        max_str = max(strs)
        min_str = min(strs)

        i = 0
        while i < len(min_str):
            if max_str[i] != min_str[i]:
                min_str = min_str[:i]
            i += 1
        return min_str





print(Solution().longest_common_prefix(["abcca", "abd", "abc"]))
print(Solution().longest_common_prefix(["flower","flow","flight"]))
print(Solution().longest_common_prefix(["dog","racecar","car"]))
print(Solution().longest_common_prefix(["a"]))
print(Solution().longest_common_prefix(["reflower","flow","flight"]))
print(Solution().longest_common_prefix(["aa","aa"]))

