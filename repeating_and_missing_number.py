def repeating_and_missing_number(arr):
    n = len(arr)
    sn = (n * (n + 1)) // 2
    s2n = (n*(n+1)*((2*n)+1)) // 6

    s, s2 = 0, 0
    for i in range(n):
        s += arr[i]
        s2 += arr[i] * arr[i]

    val_1 = s - sn
    val_2 = s2 - s2n
    val_2 = val_2 // val_1

    x = (val_1 + val_2) // 2
    y = x - val_1

    return [x,y]



print(repeating_and_missing_number([3, 1, 2, 5, 3]))
