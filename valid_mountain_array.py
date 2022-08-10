def validMountainArray(arr):
    p = 0
    q = len(arr) - 1
    peak = max(arr)
    peak_index = arr.index(peak)
    if len(arr) == 1:
        return False
    while p < peak_index:
        if arr[p] < peak:
            p += 1
        else:
            return False
    while peak_index < q:
        if arr[peak_index + 1] < peak and arr[peak_index] < len(arr) - 1:
            peak_index += 1
        else:
            return False
    return True


# print(validMountainArray([0, 1, 3, 2, 1]))
# print(validMountainArray([3, 5, 5]))
# print(validMountainArray([2, 1]))
# print(validMountainArray([2]))
print(validMountainArray([1, 3, 2]))
