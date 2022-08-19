def find_disappeared_number_in_array(arr):
    # result = []
    # new_arr = [i for i in range(1, len(arr) + 1)]
    # for i in range(0, len(arr)):
    #     if new_arr[i] not in arr:
    #         result.append(i+1)
    # return result

    missing = []
    for i in range(0, len(arr)):
        pos = abs(arr[i]) - 1
        arr[pos] = -1 * abs(arr[pos])

    for i in range(0,len(arr)):
        if arr[i] > 0:
            missing.append(i+1)
    return missing


print(find_disappeared_number_in_array([4, 3, 2, 7, 8, 2, 3, 1]))
# print(find_disappeared_number_in_array([1,1]))
# print(find_disappeared_number_in_array([2,2]))
