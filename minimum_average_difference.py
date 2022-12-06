from typing import List


def minimumAverageDifference(arr: List[int]) -> int:
    min_value = float('inf')
    index = float('inf')
    for i in range(len(arr) - 1):
        current_avg = abs((sum(arr[:i + 1]) // (i + 1)) - (sum(arr[i + 1:]) // len(arr[i + 1:])))
        if current_avg < min_value:
            min_value = current_avg
            index = i
    return index


print(minimumAverageDifference([2, 5, 3, 9, 5, 3]))
print(minimumAverageDifference([0]))
