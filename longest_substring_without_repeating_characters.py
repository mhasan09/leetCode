class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_str = 0
        dataset = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] in dataset:
                dataset.remove(s[l])
                l += 1
            else:
                dataset.add(s[r])
                r += 1
                longest_str = max(longest_str, r - l)
        return longest_str





print(Solution().lengthOfLongestSubstring("cbabcad"))