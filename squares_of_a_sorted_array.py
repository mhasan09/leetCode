def sortedSquares(arr):
    for index, i in enumerate(arr):
        if arr[index] < 0:
            arr[index] = arr[index] * (-1)
    arr.sort()
    return [i * i for i in arr]


print(sortedSquares([-7, -3, 2, 3, 11]))
