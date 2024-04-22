def find_position_of_infinite_sorted_arr(arr, target):
    low, high = 0, 1
    arr_size = 1
    while True:
        if arr[low] <= target <= arr[high]:
            return search(arr, target, low, high)
        else:
            arr_size = arr_size * 2
            low = high + 1
            high = high + arr_size


def search(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


print(find_position_of_infinite_sorted_arr([2, 3, 5, 6, 7, 8, 10, 11, 12, 15, 23, 23, 30], 15))
# print(find_position_of_infinite_sorted_arr([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], 10))
