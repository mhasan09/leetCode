def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for i in array:
        helper(threeLargest, i)
    return threeLargest


def helper(array, number):
    if array[2] is None or number > array[2]:
        shiftFunc(array, number, 2)
    elif array[1] is None or number > array[1]:
        shiftFunc(array, number, 1)
    elif array[0] is None or number > array[0]:
        shiftFunc(array, number, 0)


def shiftFunc(array, number, id):
    for i in range(id + 1):
        if i == id:
            array[i] = number
        else:
            array[i] = array[i + 1]
            print(array)


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
