def spiralTraverse(array):
    x = []
    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            x.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            x.append(array[row][endCol])
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            x.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            x.append(array[row][startCol])
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return x


print(spiralTraverse([
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]))


