from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}

        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)

        def dfs(cur, parent):
            time = 0
            for c in adj[cur]:
                if c == parent:
                    continue
                current_time = dfs(c, cur)
                if current_time or hasApple[c]:
                    time += current_time + 2
            return time

        return dfs(0, -1)


print(Solution().minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]))
