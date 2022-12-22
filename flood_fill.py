from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        current_color = image[sr][sc]

        row = len(image)
        col = len(image[0])

        if new_color == current_color:
            return image

        def dfs(r, c):
            if image[r][c] == current_color:
                image[r][c] = new_color

                # up
                if r >= 1:
                    dfs(r - 1, c)

                # down
                if r + 1 < row:
                    dfs(r + 1, c)

                # left
                if c >= 1:
                    dfs(r, c - 1)

                # right
                if c + 1 < col:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image
