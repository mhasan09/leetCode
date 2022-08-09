def remove_element(arr, val):
    p = 0
    q = len(arr) - 1
    count = 0
    while p <= q:
        if arr[p] == val and arr[q] != val:
            arr[p], arr[q] = arr[q], arr[p]
            count += 1
            p += 1
            q -= 1
        elif arr[p] == val and arr[q] == val:
            count += 1
            q -= 1
        else:
            p += 1
    return len(arr) - count




print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(remove_element([3, 2, 2, 3], 2))
