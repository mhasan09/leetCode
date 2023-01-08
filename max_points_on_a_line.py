import collections
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # If we only have 1 point then any line passes through it, so we return 1
        # If we only have 2 point then a line is the shortest path through both, so we return 2
        n = len(points)
        if n < 3:
            return n

        # We make a special helper func for finding the slope so we do not divide by 0
        def find_slope(p1, p2):
            # unpack the points into (x, y) coordinate pairs
            x1, y1 = p1
            x2, y2 = p2
            # Find the denominator or change in x
            delta_x = x1 - x2
            if delta_x == 0:
                return float('inf')
            # Slope = change in y / change in x
            return (y1 - y2) / delta_x

        # Start the answer at 1
        # since we return `ans + 1` 
        # which will be 2 if we have a skewed lattice (i.e. we actively minimize collinearity)
        ans = 1
        for i, p1 in enumerate(points):
            # For each point, create a new counter map: slope -> count of slope occurrences
            slopes = collections.defaultdict(int)
            # Now for fixed `p1`, consider all future `p2`
            # where we only look at future points to avoid double-counting
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)
                # and add one for the respective count
                slopes[slope] += 1
                # Note that we have to update `ans` inside this loop as `slope` changes every iteration
                ans = max(slopes[slope], ans)
        # Add one to account for the point itself (to have 1 line you need 2 points)
        return ans + 1


# print(Solution().maxPoints([[1, 1], [2, 2], [3, 3]]))
print(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
