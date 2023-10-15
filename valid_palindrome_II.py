class Solution:
    def compare(self, string):
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] == string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        global s1
        global s2
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s1 = s[:left] + s[left+1:]
                s2 = s[:right] + s[right+1:]

                if self.compare(s1):
                    return True
                if self.compare(s2):
                    return True

        return False

# print(Solution().validPalindrome("abccbxa"))
# print(Solution().validPalindrome("aba"))
# print(Solution().validPalindrome("abca"))
# print(Solution().validPalindrome("abc"))
# print(Solution().validPalindrome("eeccccbebaeeabebccceea"))
print(Solution().validPalindrome("acjakebdccdeedccdbeaca"))
