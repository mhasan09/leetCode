from typing import List
#
#
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if len(strs) == 0:
#             return [[""]]
#         ans = {}
#
#         for word in strs:
#             temp = ''.join(sorted(word))
#             if temp in ans:
#                 ans[temp].append(word)
#             else:
#                 ans[temp] = [word]
#         return list(ans.values())
#
#
#
# print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))