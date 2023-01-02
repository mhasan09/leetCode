class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


print(Solution().detectCapitalUse("AD"))
print(Solution().detectCapitalUse("FlaG"))  # expected: false
print(Solution().detectCapitalUse("g"))
