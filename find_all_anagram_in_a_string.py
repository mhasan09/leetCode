import collections


class Solution(object):
    def findAnagrams(self, s, p):

        data_dict_p = collections.Counter(p)
        data_dict_s = collections.Counter(s[:len(p)-1])
        output = []
        start = 0

        for i in range(len(p)-1, len(s)):
            data_dict_s[s[i]] += 1

            if data_dict_p == data_dict_s:
                output.append(start)

            data_dict_s[s[start]] -= 1

            if data_dict_s[s[start]] == 0:
                del data_dict_s[s[start]]

            start += 1

        return output






print(Solution().findAnagrams("cbaebabacd", "abc"))
# print(Solution().findAnagrams("abab", "ab"))
