from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def calculate_permutation(index, number):
            if index == len(number):
                answer.append(number[:])
                return

            for i in range(index, len(number)):
                number[index], number[i] = number[i], number[index]
                calculate_permutation(index + 1, number)
                number[index], number[i] = number[i], number[index]



        answer = []
        calculate_permutation(0, nums)
        return answer

print(Solution().permute([1, 2, 3]))
