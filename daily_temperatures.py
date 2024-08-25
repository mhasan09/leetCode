from inspect import stack
from operator import index
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                result[index] = i - index
            stack.append((temperatures[i], i))
        return result


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))  # [3,1,1,2,1,1,0,1,1,0]
