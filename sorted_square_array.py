def sortedSquaredArray(array):
    outputArray = []
    for i in range(0,len(array)):
        array[i] = array[i] * array[i]
        outputArray.append(array[i])
    outputArray.sort()
    return outputArray

print(sortedSquaredArray( [-2, -1]))
