def searchStartIndex(arr, target):
    index = -1
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            index = mid
            j = mid - 1
        elif arr[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return index


def searchEndIndex(arr, target):
    index = -1
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            index = mid
            i = mid + 1
        elif arr[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return index


def searchRange(arr, target):
    pos = [-1, -1]
    pos[0] = searchStartIndex(arr, target)
    pos[1] = searchEndIndex(arr, target)

    return pos


print(searchRange([5, 7, 7, 8, 8, 10], 6))
