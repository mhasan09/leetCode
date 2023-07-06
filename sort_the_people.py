from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = dict()
        for i in range(len(names)):
            data[heights[i]] = names[i]
        heights = sorted(heights, reverse=True)
        return [data[i] for i in heights]


print(Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))

'''

Mary, emma, john

'''