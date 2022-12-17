class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matrix = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        longest = 0
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
                longest = max(longest,matrix[i][j])
        return longest



print(Solution().longestCommonSubsequence("stone", "longest"))
