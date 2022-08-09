def remove_duplicate(arr):
    left = 0
    right = 0
    counter = 0
    while left < len(arr) - 1 and right < len(arr):
        if arr[left] == arr[right]:
            right += 1
        else:
            arr[left + 1] = arr[right]
            left += 1
            counter += 1
    return counter+1


print(remove_duplicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicate([1, 1, 2]))
