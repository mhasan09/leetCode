def intersect(arr1,arr2):
    hashmap = {}
    result = []
    for i in arr1:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    for i in arr2:
        if i in hashmap and hashmap[i] > 0:
            result.append(i)
            hashmap[i] -= 1
    return result

print(intersect([4,9,5],[9,4,9,8,4]))