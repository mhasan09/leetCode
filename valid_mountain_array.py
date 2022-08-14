def validMountainArray(arr):
    p = 0
    q = 1
    peak = max(arr)
    peak_index = arr.index(peak)
    if len(arr) == 1 or len(arr) == 2 or peak_index == 0 or peak_index == len(arr) - 1:
        return False
    while p < peak_index:
        if arr[p] < arr[q]:
            p += 1
            q += 1
        else:
            return False
    while peak_index < len(arr) - 1:
        if arr[peak_index] > arr[peak_index + 1]:
            peak_index += 1
        else:
            return False
    return True


# print(validMountainArray([0, 1, 3, 2, 1]))
# print(validMountainArray([3, 5, 5]))
# print(validMountainArray([2, 1]))
# print(validMountainArray([2]))
# print(validMountainArray([1, 3, 2]))
# print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(validMountainArray([0, 1, 3, 2, 1, 2]))
