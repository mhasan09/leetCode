import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = list(sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True))
        return [freq[i][0] for i in range(k)]

    def topKFrequent_using_heap(self, nums: List[int], k: int) -> List[int]:
        heap = []
        data = Counter(nums)
        for key,val in data.items():
            if len(heap) < k:
                heapq.heappush(heap, (val,key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]


# print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
# print(Solution().topKFrequent([3, 0, 1, 0], 1))
print(Solution().topKFrequent_using_heap([1,1,2,2,2,3,3,3,3], 2))
