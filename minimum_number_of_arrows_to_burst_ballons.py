class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        arrow = 1
        current = points[0]
        for i in range(1, len(points)):
            if current[1] >= points[i][0]:
                current = [max(current[0],points[i][0]), min(current[1],points[i][1])]
            else:
                current = points[i]
                arrow += 1
        return arrow


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
