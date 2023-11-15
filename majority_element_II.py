from typing import List


class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        element_1 = 0
        element_2 = 0
        count_1 = 0
        count_2 = 0

        for i in arr:
            if count_1 == 0 and element_2 != i:
                count_1 = 1
                element_1 = i

            elif count_2 == 0 and element_1 != i:
                count_2 = 1
                element_2 = i

            elif element_1 == i:
                count_1 += 1

            elif element_2 == i:
                count_2 += 1

            else:
                count_1 -= 1
                count_2 -= 1

        answer = []

        count_1, count_2 = 0, 0
        for i in arr:
            if i == element_1:
                count_1 += 1
            if i == element_2:
                count_2 += 1

        minimum = (len(arr) // 3) + 1
        if count_1 >= minimum:
            answer.append(element_1)
        if count_2 >= minimum:
            answer.append(element_2)
        return answer


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([1,2]))
print(Solution().majorityElement([2,2]))
