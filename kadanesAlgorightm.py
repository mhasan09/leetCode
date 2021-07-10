def kadanesAlgorithm(array):
    maxLastSum = array[0]
    maxSoFar = array[0]
    for i in range(1,len(array)):
        n = array[i]
        maxLastSum = max(n + maxLastSum,n)
        maxSoFar = max(maxLastSum, maxSoFar)
    return maxSoFar


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
