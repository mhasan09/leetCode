from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[0] * i for i in range(1, numRows + 1)]

        row_len = len(output)
        col_len = len(output[0])

        for row in range(row_len):
            for col in range(col_len):
                output[row][0] = 1
                output[row][-1] = 1

        for row in range(2,len(output)):
            for col in range(1,len(output[row])-1):
                output[row][col] = output[row-1][col-1] + output[row-1][col]

        return output

print(Solution().generate(5))