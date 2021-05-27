def moveElementToEnd(array, toMove):
    count = 0
    newArray = []
    for i in range(0, len(array)):
        if array[i] != toMove:
            newArray.append(array[i])
        else:
            count += 1
    for i in range(0, count):
        newArray.append(toMove)
    print(count)
    return newArray


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))



