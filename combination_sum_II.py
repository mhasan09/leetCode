from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        data = []

        def calculate_combination(index, target):
            if target == 0:
                answer.append(data.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                data.append(candidates[i])
                calculate_combination(i + 1, target - candidates[i])
                data.pop()

        candidates.sort()
        calculate_combination(0, target)
        return answer


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
