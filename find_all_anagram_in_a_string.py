class Solution(object):
    def findAnagrams(self, s, p):
        main_string_len = len(s)
        short_string_len = len(p)

        if main_string_len < short_string_len:
            return []

        main_string_counter, short_string_counter = {}, {}

        for i in range(short_string_len):
            short_string_counter[p[i]] = 1 + short_string_counter.get(p[i], 0)
            main_string_counter[s[i]] = 1 + main_string_counter.get(s[i], 0)

        result = [0] if short_string_counter == main_string_counter else []

        l = 0
        for r in range(short_string_len,main_string_len):
            main_string_counter[s[r]] = 1 + main_string_counter.get(s[r], 0)
            main_string_counter[s[l]] -= 1

            if main_string_counter[s[l]] == 0:
                main_string_counter.pop(s[l])

            l += 1

            if short_string_counter == main_string_counter:
                result.append(l)

        return result




print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))
