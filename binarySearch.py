def binarySearch(a,target):
    a.sort()
    print(a)
    left = 0
    right = len(a) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == a[middle]:
            return middle
        elif target > a[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1

print(binarySearch([0, 1, 3, 21, 23, 33, 45, 112],21))