from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = list(sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True))
        return [freq[i][0] for i in range(k)]



# print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([3, 0, 1, 0], 1))
