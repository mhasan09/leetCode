def containsNearbyDuplicate(arr, k):
    hashmap = {}
    for i, j in enumerate(arr):
        if j in hashmap and i - hashmap[j] <= k:
            return True
        hashmap[j] = i
    return False

print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
