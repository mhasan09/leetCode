def findClosestPair(first, second, target):
    # base case
    if not len(first) or not len(second):
        return ()
    # `x` and `y` points to the indexes of the closest pair found so far
    x = y = 0

    for i in range(len(first)):
        for j in range(len(second)):
            if abs(first[i] + second[j] - target) < abs(first[x] + second[y] - target):
                x = i
                y = j
    return first[x], second[y]
