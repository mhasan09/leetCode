from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        data = {}
        counter =0
        for i in range(len(tasks)):
            data[tasks[i]] = 1 + data.get(tasks[i], 0)

        if 1 in data.values():
            return -1

        for i in data.values():
            counter += i//3 + bool(i%3)
        return counter

print(Solution().minimumRounds([2,2,3,3,2,4,4,4,4,4]))
# print(Solution().minimumRounds("ACCC"))
# data[s[i]] = 1 + data.get(s[i], 0)