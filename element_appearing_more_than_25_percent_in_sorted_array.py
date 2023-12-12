import collections
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common(1)[0][0]


print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))