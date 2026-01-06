from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        min_matrix_item = float("inf")
        neg_number_counter = 0
        for row in matrix:
            for n in row:
                result += abs(n)
                min_matrix_item = min(min_matrix_item, abs(n))
                if n < 0:
                    neg_number_counter += 1

        if neg_number_counter & 1:
            result -= 2 * min_matrix_item

        return result


