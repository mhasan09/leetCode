from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
            we're going to traverse the list by column, for example
            ["cba", "daf", "ghi"] so it'll be c,d,g


            so the outer loop will be "rrjk" -> len(rrjk) -> 4
            and inner loop will be "r -> f -> g "

        """
        count = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
        return count

# print(Solution().minDeletionSize(["cba", "daf", "ghi"]))
print(Solution().minDeletionSize(["rrjk","furt","guzm"]))
