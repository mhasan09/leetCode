def intersection(arr1, arr2):
    hashmap = {}
    for i in list(set(arr1)):
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in list(set(arr2)):
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    result = []

    for key, value in hashmap.items():
        if value == 2:
            result.append(key)
    return result

print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
