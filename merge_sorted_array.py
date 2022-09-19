# def merge_sorted_array(arr1, m, arr2, n):
#     last = m + n - 1
#     while m > 0 and n > 0:
#         if arr1[m-1] < arr2[n-1]:
#             arr1[last] = arr2[n-1]
#             n -= 1
#         else:
#             arr1[last] = arr1[m-1]
#             m -= 1
#         last -= 1
#
#     while n > 0:
#         arr1[last] = arr2[n-1]
#         n -= 1
#         last -= 1
#
#
#
# print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(merge_sorted_array([0], 0, [1], 1))
# print(merge_sorted_array([1], 1, [], 0))


def merge_sorted_array(arr1, m, arr2, n):
    while m > 0 and n > 0:
        if arr1[m - 1] < arr2[n - 1]:
            arr1[m + n - 1] = arr2[n - 1]
            m -= 1
        else:
            arr1[m + n - 1] = arr1[m - 1]
            n -= 1
    while n > 0:
        arr1[m + n - 1] = arr2[n - 1]
        n -= 1


print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge_sorted_array([0], 0, [1], 1))
print(merge_sorted_array([1], 1, [], 0))
