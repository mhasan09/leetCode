from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        # Copy string in a traget string
        r = str(s[:])

        # This variable keep track of how much indexes is shifted
        # in resultant string w.r.t original string
        shifted = 0

        for idx, source, target in sorted(zip(indices, sources, targets)):

            # If source is present in string
            if s[idx:idx + len(source)] == source:
                # Recalibrate index for resultant string
                idx = idx + shifted

                # Add target to resultant string
                r = r[:idx] + target + r[idx + len(source):]

                # Update the shifted variable, it can be negative or positive
                shifted += len(target) - len(source)

        return r


print(Solution().findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))  # expected:"eeebffff"
# print(Solution().findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))
# print(Solution().findReplaceString("vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]))
