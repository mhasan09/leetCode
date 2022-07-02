def majorityElement(arr):
    hashmap = {}
    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1
        if hashmap[i] > len(arr)/2:
            return i


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
