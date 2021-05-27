'''
Time complexity O(n)
space complex O(n)
'''
# def firstDuplicateValue(array):
#     hashtable = {}
#     for i in range(0, len(array)):
#         if array[i] not in hashtable:
#             hashtable[array[i]] = i
#         else:
#             return array[i]
#     return -1

# print(firstDuplicateValue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

'''
Time complexity O(n)
space complex O(1)
'''
def firstDuplicateValue(array):
    for i in range(0, len(array)):
        absValue = abs(array[i])
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1

print(firstDuplicateValue([1, 2, 3, 1]))
