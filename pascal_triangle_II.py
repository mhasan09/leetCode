def generate(numRows):
    result = [[1]]
    for i in range(1, numRows + 1):
        temp = [1 for _ in range(i + 1)]
        for j in range(1, len(temp) - 1):
            temp[j] = result[-1][j] + result[-1][j - 1]
        result.append(temp)
    return result[-1]

print(generate(3))
