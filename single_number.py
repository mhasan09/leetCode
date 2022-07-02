def singleNumber(arr):
    a = 0
    for i in arr:
        a ^= i
    return a



print(singleNumber([2, 2, 1]))
