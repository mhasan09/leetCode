import collections
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        data = collections.Counter(nums) # ({1: 3, 3: 2, 4: 1, 2: 1})
        data_arr = collections.defaultdict(list) # defaultdict(<class 'list'>, {})
        for k, v in data.items():
            for i in range(v):
                data_arr[i].append(k) # defaultdict(<class 'list'>, {0: [1, 3, 4], 1: [1, 3], 2: [1]})
        return list(data_arr.values())

print(Solution().findMatrix([1, 3, 4, 1, 2, 3, 1]))
