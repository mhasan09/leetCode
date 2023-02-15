from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = 0
        for i in num:
            result = 10 * result + i

        return [int(i) for i in str(k+result)]


print(Solution().addToArrayForm([1, 2, 0, 0], 34))
