class Solution(object):
    def setZeroes(self, matrix):
        data = []
        for i_r, i in enumerate(matrix):
            for i_c, j in enumerate(i):
                if j == 0:
                    data.append((i_r,i_c))

        print(data)

        for row in matrix:
            for i,j in data:
                matrix[i] = [0 for _ in range(len(matrix[0]))]
                row[j] = 0

        return matrix

print(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 0, 2], [1, 3, 1, 5]]))