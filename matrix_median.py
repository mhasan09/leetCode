def matrix_median(matrix, r, c):
    low = float('inf')
    high = float('-inf')
    for i in range(len(matrix)):
        low = min(low, matrix[i][0])
        high = max(high, matrix[i][-1])

    desired = (r * c + 1) // 2

    while low < high:
        mid = low + (high - low) // 2
        count = 0
        for i in range(len(matrix)):
            count += check_boundary(matrix[i], mid)
        if count < desired:
            low = mid + 1
        else:
            high = mid

    return low


def check_boundary(row, mid):
    low, high = 0, len(row) - 1
    while low <= high:
        current_mid = low + (high - low) // 2
        if row[current_mid] <= mid:
            low = current_mid + 1
        else:
            high = current_mid - 1
    return low


print(matrix_median([[1, 5, 9, 11, 13], [2, 3, 4, 16, 19], [5, 11, 19, 21, 23]], 3, 5))
print(matrix_median([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 3, 3))
