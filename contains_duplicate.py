def contains_duplicate(arr):
    data = {}
    for i in arr:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    print(data)

    for i in data:
        if data[i] > 1:
            return True
        else:
            continue
    return False



# print(contains_duplicate([1, 2, 3, 1]))
# print(contains_duplicate([2, 14, 18, 22, 22]))
print(contains_duplicate([1, 2, 3, 4]))
# print(contains_duplicate([0, 4, 5, 0, 3, 6]))
