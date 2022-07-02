def searchInsert(arr, target):
    l, r = 0, len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(searchInsert([1, 3, 5, 6], 2))
