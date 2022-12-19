class Solution:
    def longestPalindrome(self, s: str) -> int:
        data = {}
        answer = []
        odd = 0
        for i in s:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        for i in data.values():
            answer.append(i)
            if i%2 != 0:
                odd += 1
        print(odd)
        print(answer)
        print(sum(answer))
        if odd == 0:
            return sum(answer)
        else:
            return sum(answer) - odd + 1


# print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("madamx"))