def findMaxConsecutiveOnes(arr):
    current = 0
    max_sum = 0
    for i in arr:
        if i == 1:
            current += 1
            if current > max_sum:
                max_sum = current
        else:
            current = 0

    return max_sum


print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
# print(fiMaxConsecutiveOnes([0, 1, 2, 3, 4, 5]))

"""
     [1,1,0,1,1,1]
     3
     
     [1,0,1,1,0,1]
     2
     
"""
