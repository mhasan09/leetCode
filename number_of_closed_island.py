from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if grid[i][j] == 1:
                return True
            if i <= 0 or i >= m - 1 and j <= 0 or j >= n - 1:
                return False

            grid[i][j] = 1

            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return left and right and up and down

        m = len(grid)
        n = len(grid[0])
        c = 0

        for i in range(0, m - 1):
            for j in range(0, n - 1):
                if grid[i][j] == 0 and dfs(i, j):
                    c += 1
        return c


print(Solution().closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))
