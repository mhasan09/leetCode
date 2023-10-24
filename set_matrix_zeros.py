import pprint
class Solution(object):
    def setZeroes(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # only the first row and col will be updated as zero if condition meets
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1,row_len):
            for col in range(1,col_len):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            for col in range(col_len):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(row_len):
                matrix[row][0] = 0

        return matrix



print(Solution().setZeroes([[0, 1, 2, 0],
                            [3, 4, 0, 2],
                            [1, 3, 1, 5]]))