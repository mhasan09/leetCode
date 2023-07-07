from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = dict()
        for i in range(len(names)):
            data[heights[i]] = names[i]
        heights = sorted(heights, reverse=True)
        return [data[i] for i in heights]


    def sortPeopleLambda(self, names: List[str], heights: List[int]) -> List[str]:
        data = list(zip(names, heights))
        data = sorted(data, key=lambda x:x[1], reverse=True)
        return [i[0] for i in data]


print(Solution().sortPeopleLambda(["Mary", "John", "Emma"], [180, 165, 170]))

