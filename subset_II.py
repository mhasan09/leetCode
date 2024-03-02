from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        data = []

        def calculate_subset(index):
            ans.append(data.copy())
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                data.append(nums[i])
                calculate_subset(index=i + 1)
                data.pop()

        nums.sort()
        calculate_subset(0)
        return ans


print(Solution().subsetsWithDup([1, 2, 2]))
