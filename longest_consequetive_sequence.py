from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr_set = set(nums)
        longest = 0
        for i in arr_set:
            if i - 1 not in arr_set:
                current_num = i
                current_seq = 1
                while current_num + 1 in arr_set:
                    current_seq += 1
                    current_num += 1
                longest = max(longest, current_seq)
        return longest



print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
