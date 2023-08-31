import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        ransom_note_counter = collections.Counter(ransomNote)
        magazine_counter = collections.Counter(magazine)

        for i in ransomNote:
            if i not in magazine_counter:
                return False

            if magazine_counter[i] >= ransom_note_counter[i]:
                magazine_counter[i] -= 1
                ransom_note_counter[i] -= 1
            else:
                return False

        return True



print(Solution().canConstruct("a","b"))
print(Solution().canConstruct("aa","ab"))
print(Solution().canConstruct("aa","aab"))
print(Solution().canConstruct("abxv","abxazbv"))