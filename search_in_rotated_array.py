def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r-l)//2
        if target == nums[m]:
            return m
        # check if the value is the left part
        if nums[l] <= nums[m]:
            # check for ascending order
            if nums[l] <= target <= nums[m]:
                # drag the right part
                r = m - 1
            else:
                l = m + 1
        else:
            # again check for ascending order
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1


# print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([1,3], 3))
