def validSubsequence(array, sub):
    subId = 0
    arrayId = 0
    while subId < len(sub) and arrayId < len(array):
        if sub[subId] == array[arrayId]:
            subId += 1
        arrayId += 1
    return subId == len(sub)

    # subId = 0
    # for i in range(0, len(array)):
    #     if sub[subId] == array[i]:
    #         subId += 1
    #
    #     else:
    #         return False
    # return subId == len(sub)


print(validSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 8]))
