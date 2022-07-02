def removeElement(arr, val):
    count = 0
    p, q = 0, len(arr) - 1
    while p <= q:
        if arr[p] == val:
            arr[p], arr[q] = arr[q], arr[p]
            q -= 1
            count += 1
        else:
            p += 1
    finalCount = len(arr) - count
    return finalCount


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
