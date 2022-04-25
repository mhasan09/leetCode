def removeDuplicates(nums):
    l = 0
    for r in range(1, len(nums)):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]
    return l + 1


print(removeDuplicates([1, 1, 2]))
