def merge_sorted_array(arr1, m, arr2, n):
    arr1 = arr1[:m]
    arr2 = arr2[:n]
    arr1 = sorted(arr1 + arr2)
    return arr1


print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge_sorted_array([0], 0, [1], 1))
print(merge_sorted_array([1], 1, [], 0))
