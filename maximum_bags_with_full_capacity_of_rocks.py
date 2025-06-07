from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        extra_bags = []
        for i in range(len(capacity)):
            extra_bags.append(capacity[i] - rocks[i])
        extra_bags = sorted(extra_bags)

        for i in range(len(extra_bags)):
            if additionalRocks > 0:
                if extra_bags[i] != 0 and additionalRocks >= extra_bags[i]:
                    additionalRocks -= extra_bags[i]
                    extra_bags[i] = 0

        return sum(1 for i in extra_bags if i == 0)

        # full_bag = 0
        # for i in extra_bags:
        #     if i == 0:
        #         full_bag += 1
        # return full_bag


# print(Solution().maximumBags([8, 10, 5, 9], [4, 5, 5, 8], 9))
# print(Solution().maximumBags([10, 2, 2], [2, 2, 0], 100))
print(Solution().maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))
