class Solution:
    def convert(self, inputString, numRows):
        if numRows == 1:
            return inputString

        rows = [''] * min(numRows, len(inputString))
        direction, current_row = -1, 0

        for char in inputString:
            rows[current_row] += char
            current_row += 1 if direction == -1 else -1

            if current_row == 0 or current_row == numRows - 1:
                direction = -direction

        return ''.join(rows)


# print(Solution().convert("ROLLBACK", 3))
print(Solution().convert("EMPOWERMENT", 4))
