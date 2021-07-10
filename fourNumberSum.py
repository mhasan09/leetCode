def fourNumberSum(array, targetSum):
    quadrable = []
    sumDict = {}
    for i in range(1, len(array)):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in sumDict:
                for pair in sumDict[difference]:
                    quadrable.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[k] + array[i]
            if currentSum not in sumDict:
                sumDict[currentSum] = [[array[k], array[i]]]
            else:
                sumDict[currentSum].append([array[k], array[i]])
    return quadrable


print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))
