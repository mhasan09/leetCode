def rotate_image(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


print(rotate_image([[5, 1, 9, 11],
                    [2, 4, 8, 10],
                    [13, 3, 6, 7],
                    [15, 14, 12, 16]
                    ]))


