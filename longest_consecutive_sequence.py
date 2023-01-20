from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            nums.sort()
            count = 1
            max_count = 1
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1]:
                    continue
                elif nums[i] == nums[i - 1] + 1:
                    count += 1
                else:
                    count = 1
                max_count = max(count, max_count)
            return max_count

    def longestConsecutive_2(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in num_set:
            if i - 1 not in num_set:
                length = 0
                while length + i in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


# print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
print(Solution().longestConsecutive([1, 2, 0, 1]))
# [0, 1, 1, 2]
# [ 0,  1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
