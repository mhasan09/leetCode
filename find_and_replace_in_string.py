from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        lookup = {i: (src, target) for i, src, target in zip(indices, sources, targets)}
        i, result = 0, ""
        while i < len(s):
            if i in lookup and s[i:].startswith(lookup[i][0]):
                result += lookup[i][1]
                i += len(lookup[i][0])
            else:
                result += s[i]
                i += 1
        return result


# print(Solution().findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))  # expected:"eeebffff"
# print(Solution().findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))
print(Solution().findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]))
