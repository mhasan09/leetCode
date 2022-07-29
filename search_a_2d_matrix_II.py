def search2dMatrixII(matrix, target):
    h, w = len(matrix), len(matrix[0])
    for i in matrix:
        if i[0] <= target <= i[-1]:
            l, r = 0, w - 1
            while l <= r:
                middle = (l + r) // 2
                if i[middle] < target:
                    l = middle + 1
                elif i[middle] > target:
                    r = middle - 1
                else:
                    return True
    return False


print(search2dMatrixII([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
