# def isMonotonic(array):
#     first = 0
#     last = len(array) - 1
#     if len(array) == 1 or len(array) == 0:
#         return True
#     if array[first] != array[last] and array[first] < array[last]:
#         status = "Increasing"
#     elif array[first] != array[last] and array[first] > array[last]:
#         status = "Decreasing"
#     else:
#         status = False
#
#     for i in range(0, len(array) - 1):
#         if status == "Increasing" and array[i] < array[i + 1]:
#             return True
#         if status == "Decreasing" and array[i] > array[i + 1]:
#             return True
#         else:
#             return False
#
#
# print(isMonotonic([1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]))


def isMonotonic(array):
    isDecreasing = True
    isIncreasing = True

    for i in range(0, len(array)-1):
        if array[i] < array[i + 1]:
            isDecreasing = False
        if array[i] > array[i + 1]:
            isIncreasing = False
    return isDecreasing or isIncreasing


print(isMonotonic([-1, -1, 2 , 100, 1]))

