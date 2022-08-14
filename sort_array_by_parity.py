def sort_array_by_parity(arr):
    p = 0
    q = len(arr) - 1
    while p < q:
        if arr[p] % 2 > arr[q] % 2:
            arr[p], arr[q] = arr[q], arr[p]
        if arr[p] % 2 == 0:
            p += 1
        if arr[q] % 2 != 0:
            q -= 1
    return arr



# print(sort_array_by_parity([3, 1, 2, 4]))
print(sort_array_by_parity([0, 1, 3]))
