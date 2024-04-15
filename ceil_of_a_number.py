def ceil_of_a_number(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return arr[mid]
    return arr[low]


print(ceil_of_a_number([2,3,5,9,14,16,18], 4))