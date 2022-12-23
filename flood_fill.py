from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        current_color = image[sr][sc]
        row = len(image)
        col = len(image[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r > row - 1 or c > col - 1 or image[r][c] != current_color or image[r][c] == new_color:
                return

            image[r][c] = new_color

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image
