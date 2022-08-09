def checkIfExist(arr):
    double_arr = {}
    if arr.count(0) > 1:
        return True
    for i in arr:
        if i != 0:
            double_arr[i * 2] = i
    for i in double_arr:
        if i not in arr:
            continue
        else:
            return True
    return False


# print(checkIfExist([10, 2, 5, 3]))
# print(checkIfExist([7, 1, 14, 11]))
# print(checkIfExist([3, 1, 7, 11]))
print(checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
# print(checkIfExist([0, 0]))
# print(checkIfExist([0, 3, 6]))
