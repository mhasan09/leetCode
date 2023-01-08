from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = idx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, idx = 0, i+1

        return idx


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(Solution().canCompleteCircuit([1, 2, 3, 4, 5, 5, 70], [2, 3, 4, 3, 9, 6, 2]))
