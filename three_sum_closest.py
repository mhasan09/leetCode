def three_sum_closest(array, target):
    array.sort()
    min_target = float("inf")
    min_difference = float("inf")

    for i in range(0, len(array) - 1):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            current_diff = (current_sum - target)
            if abs(min_difference) > abs(current_diff):
                min_difference = current_diff
                min_target = current_sum
            if current_diff == 0:
                return current_sum
            elif current_diff > 0:
                right -= 1
            else:
                left += 1

    return min_target


# print(three_sum_closest([1, 2, 3, 4, 5, 6, 11], 10))
# print(three_sum_closest([-1, 2, 1, -4], 1))
# print(three_sum_closest([1, 1, 1, 0], -100))
print(three_sum_closest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))
