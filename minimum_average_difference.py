from typing import List


def minimumAverageDifference(arr: List[int]) -> int:
    total_sum = sum(arr)
    min_diff = float('inf')
    index = 0
    current_sum = 0
    for i in range(len(arr)):
        if i != len(arr) - 1:
            current_sum = current_sum + arr[i]
            at_beginning = current_sum // (i + 1)
            final_diff = (total_sum - current_sum) // (len(arr) - (i + 1))
            current_diff = abs(final_diff - at_beginning)
            if current_diff < min_diff:
                min_diff = current_diff
                index = i
        else:
            current_sum = total_sum
            at_beginning = current_sum // len(arr)
            final_diff = (total_sum - current_sum) // len(arr)
            current_diff = abs(final_diff - at_beginning)
            if current_diff < min_diff:
                min_diff = current_diff
                index = i
    return index


# print(minimumAverageDifference([2, 5, 3, 9, 5, 3]))
# print(minimumAverageDifference([0]))
print(minimumAverageDifference([4, 2, 0]))
