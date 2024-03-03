from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        data = []

        def calculate_combination(index, target):
            if index == len(candidates):
                if target == 0:
                    ans.append(data.copy())
                return

            if candidates[index] <= target:
                data.append(candidates[index])
                calculate_combination(index, target - candidates[index])
                data.pop()

            calculate_combination(index + 1, target)

        calculate_combination(0, target)
        return ans


print(Solution().combinationSum([2, 3, 6, 7], 7))
