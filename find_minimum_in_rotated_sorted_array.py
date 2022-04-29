def findMin(nums):
    result = nums[0]  # setting the minimum value into a var
    l, r = 0, len(nums) - 1  # setting up the pointer
    while l <= r:  # binary search
        if nums[l] < nums[r]:
            result = min(result, nums[l])  # if array is already sorted then break
            break
        mid = (l + r) // 2  # setting up the middle value
        result = min(result, nums[mid])  # compare the result with the mid value
        if nums[mid] >= nums[l]:  # if mid value bigger then go right
            l = mid + 1  # by going right we've to set the left value to 1 index right again
        else:
            r = mid - 1  # else mid value is lesser then right then go left
    return result


print(findMin([3, 4, 5, 1, 2]))


