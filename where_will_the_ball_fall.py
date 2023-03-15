from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # Get the number of rows and columns in the grid
        row_len, col_len = len(grid), len(grid[0])
        # Initialize the result list with -1 for each ball
        result = [-1] * col_len

        # Iterate through each ball in the top row of the grid
        for j in range(col_len):
            # Initialize the starting row index and column index for the current ball
            row = 0
            col = j
            # Simulate the movement of the ball from the top row to the bottom row of the grid, row by row
            while row < row_len:
                # Check if the current cell has a diagonal board pointing right
                if grid[row][col] == 1:
                    # If the ball hits the right wall or a diagonal board pointing left, it gets stuck
                    if col == col_len - 1 or grid[row][col + 1] == -1:
                        break
                    # Otherwise, the ball bounces off to the right
                    col += 1
                # Check if the current cell has a diagonal board pointing left
                else:
                    # If the ball hits the left wall or a diagonal board pointing right, it gets stuck
                    if col == 0 or grid[row][col - 1] == 1:
                        break
                    # Otherwise, the ball bounces off to the left
                    col -= 1
                # Move the ball down to the next row
                row += 1

            # If the ball falls off the bottom row, update the result list with the column index where it falls off
            if row == row_len:
                result[j] = col

        # Return the result list with the column index where each ball falls off or -1 if the ball gets stuck
        return result


print(Solution().findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]))
