class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        data = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        longest = 0
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:
                    data[i][j] = 1 + data[i-1][j-1]
                else:
                    data[i][j] = max(data[i-1][j], data[i][j-1])
                longest = max(longest, data[i][j])
        return longest


print(Solution().longestCommonSubsequence("stone", "longest"))
