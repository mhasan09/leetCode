from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_number = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_number += 1
                    self.dfs(grid,i,j)
        return island_number



    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "2"
        self.dfs(grid, i+1, j) # down
        self.dfs(grid, i-1, j) # up
        self.dfs(grid, i, j+1) #  right
        self.dfs(grid, i, j-1) # left


print(Solution().numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
))

print(Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
))
