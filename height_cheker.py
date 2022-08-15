def height_checker(arr):
    new_arr = arr.copy()
    new_arr.sort()
    counter = 0
    for i in range(0, len(arr)):
        if arr[i] != new_arr[i]:
            counter += 1
    return counter


print(height_checker([1, 1, 4, 2, 1, 3]))
print(height_checker([5, 1, 2, 3, 4]))
