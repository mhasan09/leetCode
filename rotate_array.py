def rotate_array(arr, k):
    for i in range(0, k):
        arr.insert(0, arr[len(arr) - 1])
        del arr[-1]
    return arr


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_array([-1, -100, 3, 99], 2))
