from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_1 = nums[:n]
        nums_2 = nums[n:]
        output = []
        for i in range(len(nums_2)):
            output.append(nums_1[i])
            output.append(nums_2[i])
        return output


print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3))
