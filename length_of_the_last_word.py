class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
print(Solution().lengthOfLastWord("luffy is still joyboy"))
