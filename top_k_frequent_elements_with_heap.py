from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)
        heap = []
        for num,freq in data.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq,num))
            else:
                heapq.heappushpop(heap, (freq, num))
        return [t[1] for t in heap]


print(Solution().topKFrequent([1,1,1,2,2,3], 2))