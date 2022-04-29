def productExceptSelf(nums):
    result = [1] * len(nums)  # [1,1,1,1]
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix  # for first case [1*1]
        prefix *= nums[i]  # setting the value of prefix

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):  # reverse order for postfix
        result[i] *= postfix  # for the last case and multiply it to the array value
        postfix *= nums[i]  # set the value of postfix
    return result


print(productExceptSelf([1, 2, 3, 4]))
