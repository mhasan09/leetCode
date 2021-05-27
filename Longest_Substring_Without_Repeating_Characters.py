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




# string = "alamgir"
# string = list(string)
# longest = [0,1]
# startingIndex = 0
# hashTable = {}
#
# for i,char in enumerate(string):
#     if char in hashTable:
#         startingIndex = max(startingIndex, hashTable[char] + 1)
#     if longest[1] - longest[0] < i - startingIndex + 1:
#         longest = [startingIndex,i+1]
#     hashTable[char] = i
#
# pp = string[longest[0]:longest[1]]
# xx = ('').join(pp)
# print(xx)
# print(len(xx))


