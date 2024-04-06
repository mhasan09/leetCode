from typing import List


class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        i, j = 0, 0
        n = len(arr1) + len(arr2)


        index_1 = (n // 2) - 1
        index_2 = n // 2
        counter = 0
        answer_index_1 = -1
        answer_index_2 = -1
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                 if counter == index_1:
                     answer_index_1 = arr1[i]

                 if counter == index_2:
                     answer_index_2 = arr1[i]
                 i += 1

            else:
                if counter == index_1:
                    answer_index_1 = arr2[j]

                if counter == index_2:
                    answer_index_2 = arr2[j]

                j += 1

            counter += 1

        while i < len(arr1):
            if counter == index_1:
                answer_index_1 = arr1[i]

            if counter == index_2:
                answer_index_2 = arr1[i]

            i += 1
            counter += 1

        while j < len(arr2):
            if counter == index_1:
                answer_index_1 = arr2[j]

            if counter == index_2:
                answer_index_2 = arr2[j]

            j += 1
            counter += 1



        if n % 2 == 0:
            return (answer_index_1 + answer_index_2) / 2
        return answer_index_2





# print(Solution().findMedianSortedArrays([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
# print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3,4]))
