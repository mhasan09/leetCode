def plusOne(arr):
    for i in reversed(range(len(arr))):
        if arr[i] != 9:
            arr[i] += 1
            break
        else:
            arr[i] = 0
    if arr[0] == 0:
        arr.insert(0,1)
    return arr


print(plusOne([4, 3, 2, 1]))
