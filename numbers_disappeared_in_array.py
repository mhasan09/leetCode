def disappear(arr):
    n = len(arr)
    a = [i + 1 for i in range(n)]
    return list(set(a) - set(arr))


print(disappear([4, 3, 2, 7, 8, 2, 3, 1]))