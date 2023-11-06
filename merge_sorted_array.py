def merge_sorted_array(arr1, m, arr2, n):
    a, b, write_index = m-1, n-1, m+n-1
    while b >= 0:
        if a>=0 and arr1[a] > arr2[b]:
            arr1[write_index] = arr1[a]
            a -= 1
        else:
            arr1[write_index] = arr2[b]
            b -= 1
        write_index -= 1


print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# print(merge_sorted_array([0], 0, [1], 1))
# print(merge_sorted_array([1], 1, [], 0))
