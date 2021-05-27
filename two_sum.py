# string = [2,7,11,15,3]
# target = 10
# b = []
# for i in range(len(string)-1):
#     for j in range(i+1,len(string)):
#         if (string[i]+string[j] == target):
#             b.append(i)
#             b.append(j)
#             j= j+1
#     i = i+1
#
#
#
# print(b)

def twoNumberSum(array, targetSum):
    outputArr = []
    array.sort()
    left = 0
    right = len(array) - 1
    for i in range(0, len(array) - 1):
        if array[left] + array[right] > targetSum:
            right -= 1
        elif array[left] + array[right] < targetSum:
            left += 1
        elif array[left] + array[right] == targetSum:
            outputArr.append(left)
            outputArr.append(right)
            return outputArr
    return []
print(twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],164))