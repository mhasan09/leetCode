'''
def arrayInProduct(array):
    productArray = []
    finalProductArray = []
    total = 1
    for i in range(len(array)):
        total = total * array[i]

    for i in range(len(array)):
        productArray.append(total)

    for i in range(len(productArray)):
        productArray[i] = productArray[i] / array[i]
        finalProductArray.append(int(productArray[i]))
    return finalProductArray

print(arrayInProduct([5, 1, 8, 2]))
'''


def arrayInProduct(array):
    leftProduct = 1
    rightProduct = 1
    leftArray = [1 for _ in range(len(array))]
    rightArray = [1 for _ in range(len(array))]
    mainArray = [1 for _ in range(len(array))]

    for i in range(len(array)):
        leftArray[i] = leftProduct
        leftProduct *= array[i]
    for i in reversed(range(len(array))):
        rightArray[i] = rightProduct
        rightProduct *= array[i]
    for i in range(len(array)):
        mainArray[i] = leftArray[i] * rightArray[i]
    return mainArray

print(arrayInProduct([5,1,4,2]))

