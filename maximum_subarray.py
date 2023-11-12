# def maxSubArray(arr):
#     total_sum = arr[0]
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             current = 0
#             for k in range(i, j):
#                 current = current + arr[k]
#                 total_sum = max(current, total_sum)
#     return total_sum

def maxSubArray(arr):
    maximum = arr[0]
    current = 0
    for i in arr:
        if current + i < i:
            current = i
        else:
            current += i
        maximum = max(current,maximum)
    return maximum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
