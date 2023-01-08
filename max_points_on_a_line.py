import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            delta_x = x1 - x2
            if delta_x == 0:
                return float('inf')
            return (y1 - y2) / delta_x

        ans = 1
        for i, p1 in enumerate(points):
            slopes = collections.defaultdict(int)
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1


print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
