class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_counter = {}
        s2_counter = {}

        for i in s1:
            s1_counter[i] = 1 + s1_counter.get(i, 0)

        start = 0

        for end, char in enumerate(s2):
            s2_counter[char] = 1 + s2_counter.get(char, 0)

            if end - start + 1 == len(s1):
                if s1_counter == s2_counter:
                    return True

                else:
                    if s2_counter[s2[start]] == 1:
                        del s2_counter[s2[start]]
                    else:
                        s2_counter[s2[start]] -= 1
                    start += 1
        return False

print(Solution().checkInclusion("ab", "eidbaooo"))
print(Solution().checkInclusion("ab", "eidboaoo"))

