def longestPalindrome(s: str) -> str:
    dp = [[False] * len(s) for _ in range(len(s))]
    ans = s[0]

    for i in range(0, len(s)):
        dp[i][i] = True

    for i in reversed(range(0, len(s)-1)):
        for j in range(i, len(s)):
            if s[i] == s[j] and (dp[i + 1][j - 1] or i == j - 1):
                dp[i][j] = True
                if len(ans) < j - i + 1:
                    ans = s[i:j+1]

    return ans


print(longestPalindrome("aabaaracecar"))
