def intersect(arr1, arr2):
    data = {}
    result = []
    for i in arr1:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    for i in arr2:
        if i in data and data[i] > 0:
            result.append(i)
            data[i] -= 1
        else:
            continue
    return result


print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
