from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int):
        data = defaultdict(list)
        for u, v in edges:
            data[u].append(v)
            data[v].append(u)

        ...

print(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
