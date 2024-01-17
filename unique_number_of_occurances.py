import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        data = collections.Counter(arr)
        return len(set(data.values())) == len(list(data.values()))


print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
