from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        i, j = 0, 1
        while i < len(temperatures):
            if j >= len(temperatures):
                result.append(0)
                return result
            if temperatures[i] < temperatures[j]:
                result.append(j - i)
                i += 1
                j = i + 1

            else:
                j += 1
                if j >= len(temperatures):
                    result.append(0)
                    i += 1
                    j = i + 1
        return result


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))  # [3,1,1,2,1,1,0,1,1,0]
