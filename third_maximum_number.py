def third_max(arr):
    arr = list(set(arr))
    arr.sort()
    if len(arr) <= 2:
        return max(arr)
    return arr[len(arr) - 3]


# print(third_max([2, 2, 3, 1]))
print(third_max([-1, 2, 3]))
# print(third_max([1, 2]))
