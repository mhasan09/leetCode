import heapq
class MedianFinder:
    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        # add to small heap
        heapq.heappush(self.small_heap, -1 * num)

        # check every element of large heap > small heap
        if self.small_heap and self.large_heap and ((-1 * self.small_heap[0]) > self.large_heap[0]):
            value = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, value)

        # uneven heap size
        if len(self.small_heap) > len(self.large_heap) + 1:
            value = -1 * heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, value)

        if len(self.small_heap) + 1 < len(self.large_heap):
            value = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, -1 * value)

    def findMedian(self) -> float:
        # odd case for small and large
        if len(self.small_heap) > len(self.large_heap):
            return -1 * self.small_heap[0]

        if len(self.small_heap) < len(self.large_heap):
            return self.large_heap[0]

        # even case
        return (-1 * self.small_heap[0] + self.large_heap[0] ) / 2