from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordMap = {}
        res = 0
        for word in words:
            if wordMap.get(word[::-1], 0):
                res += 4
                wordMap[word[::-1]] -= 1
            else:
                wordMap[word] = 1 + wordMap.get(word, 0)

        # same letter in a word case "aa" / "bb"
        for word in wordMap:
            if word[0] == word[1] and wordMap[word] > 0:
                res += 2
                break
        return res


print(Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
