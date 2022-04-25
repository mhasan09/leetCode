def containsDuplicate(num):
    hashmap = {}
    for i in num:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    print(hashmap)
    for i in hashmap:
        if hashmap[i] > 1:
            return True
    return False
print(containsDuplicate([2,14,18,22,22]))

