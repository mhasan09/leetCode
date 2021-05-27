def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pointerA = 0
    pointerB = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while pointerA < len(arrayOne) and pointerB < len(arrayTwo):
        n1 = arrayOne[pointerA]
        n2 = arrayTwo[pointerB]
        if n1 < n2:
            current = n2 - n1
            pointerA += 1
        elif n1 > n2:
            current = n1 - n2
            pointerB += 1
        else:
            return [n1, n2]
        if smallest > current:
            smallest = current
            smallestPair = [n1,n2]

    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
