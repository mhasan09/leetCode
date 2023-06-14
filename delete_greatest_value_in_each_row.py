from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        max_item = 0
        arr = []
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                arr.append(max(grid[j]))
                grid[j].remove(max(grid[j]))
            max_item += max(arr)
            arr.clear()
        return max_item

print(Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
print(Solution().deleteGreatestValue([[10]]))


