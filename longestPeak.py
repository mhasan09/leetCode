def longestPeak(array):
    result = 0
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            left = right = i
            while left > 0 and array[left] > array[left - 1]:
                left -= 1
            while right < len(array) - 1 and array[right] > array[right + 1]:
                right += 1
            result = max(result, (right - left + 1))
    return result


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))

# def longestPeak(array):
#     res = 0
#
#     for indx in range(1, len(array) - 1):
#         if array[indx - 1] < array[indx] > array[indx + 1]:
#
#             l = r = indx
#
#             while l > 0 and array[l] > array[l - 1]:
#                 l -= 1
#
#             while r + 1 < len(array) and array[r] > array[r + 1]:
#                 r += 1
#
#             res = max(res, (r - l + 1))
#
#     return res
#
# print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
