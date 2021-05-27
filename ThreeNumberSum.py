def threeNumberSum(array, targetSum):
    array.sort()
    resultArray = []
    for i in range(0, len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                resultArray.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return resultArray


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
