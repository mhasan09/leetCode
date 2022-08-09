def validMountainArray(arr):
    i = 0
    p = 0
    q = len(arr) - 1
    m = (p + q) // 2
    while i < len(arr):
        left = arr[m-1]
        right = arr[m+1]
        if left <= arr[m] >= right:
            left -= 1
            right += 1
        else:
            return False
    return True


print(validMountainArray([0, 3, 2, 1]))
# print(validMountainArray([3, 5, 5]))
# print(validMountainArray([2, 1]))
