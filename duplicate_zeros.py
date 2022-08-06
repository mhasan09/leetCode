def duplicateZeros(arr):
    i = 0
    j = len(arr)
    while i < j - 1:
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            del arr[len(arr)-1]
            i += 2
        else:
            i += 1
    return arr


print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicateZeros([1, 2, 3]))
print(duplicateZeros([1, 0, 2, 3]))
