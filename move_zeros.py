def moveZeroes(arr):
    l = 0
    for r in range(len(arr)):
        if arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1

    return arr


print(moveZeroes([0, 1, 0, 3, 12]))
