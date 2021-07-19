def largestRange(array):
    longestRange = 0
    bestRange = []
    nums_dictionary = {}
    for i in array:
        nums_dictionary[i] = True
    for i in array:
        if not nums_dictionary[i]:
            continue
        nums_dictionary[i] = False
        currentLength = 1
        left = i - 1
        right = i + 1
        while left in nums_dictionary:
            nums_dictionary[left] = False
            currentLength += 1
            left -= 1
        while right in nums_dictionary:
            nums_dictionary[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestRange:
            longestRange = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
