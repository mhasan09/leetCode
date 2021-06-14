a = "clementisacap"
a = list(a)
print(len(a))
maximum_length = 0
startingIndex = 0
hashTable = {}
for i in range(0, len(a)):
    if a[i] in hashTable:
        startingIndex = max(startingIndex, hashTable[a[i]] + 1)
    hashTable[a[i]] = i
    maximum_length = max(maximum_length, i - startingIndex + 1)

print(maximum_length)




