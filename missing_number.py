def missingNumber(arr):
    n = len(arr) + 1
    sum_ = (n/2) * (n-1)
    return sum_ - sum(arr)


print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
