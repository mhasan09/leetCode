class Solution:
    def calculate_paths(self, i, j, m, n, data):
        # check whether we're in the last cell
        if i == m - 1 and j == n - 1:
            return 1

        # check whether it's already computed or not
        if data[i][j] != -1:
            return data[i][j]

        right_path, down_path = 0, 0
        if i < m - 1:
            right_path = self.calculate_paths(i+1, j, m, n, data)

        if j < n - 1:
            down_path = self.calculate_paths(i, j+1, m, n, data)

        data[i][j] = right_path + down_path
        return data[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        data = [[-1 for _ in range(n)] for _ in range(m)]
        return self.calculate_paths(0, 0, m, n, data)


print(Solution().uniquePaths(3, 2))
