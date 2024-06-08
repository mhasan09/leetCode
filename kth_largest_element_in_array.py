import heapq
from typing import List



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []
        for i in range(len(nums)):
            self.push(data, nums[i])
        item = 0
        for i in range(k):
            item = heapq.heappop(data)
        return item*(-1)


    def push(self, heap, item):
        return heapq.heappush(heap, -item)



print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))