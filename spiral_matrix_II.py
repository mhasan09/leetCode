class Solution:
    def generateMatrix(self, n: int):
        # creating the nxn matrix first
        matrix = [[0]*n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        counter = 1
        while left <= right:
            # top row
            for c in range(left, right + 1):
                matrix[top][c] = counter
                counter += 1
            top += 1

            # right col
            for r in range(top, bottom + 1):
                matrix[r][right] = counter
                counter += 1
            right -= 1

            # bottom row (reverse)
            for c in range(right, left-1, -1):
                matrix[bottom][c] = counter
                counter += 1
            bottom -= 1

            # left col (reverse)
            for r in range(bottom, top-1, -1):
                matrix[r][left] = counter
                counter += 1
            left += 1

        return matrix


print(Solution().generateMatrix(4))