class Solution:
    def majorityElement(self, nums):
        """ using moore's voting algorithm """
        n = len(nums)
        count = 0
        candidate = None

        for i in range(n):
            if count == 0:
                count = 1
                candidate = nums[i]
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1

        # checking if the stored element is the majority element
        count_1 = 0
        for i in range(n):
            if nums[i] == candidate:
                count_1 += 1

        if count_1 > (n / 2):
            return candidate
        return -1


print(Solution().majorityElement([2, 2, 1, 1, 4, 4, 1, 1, 5]))
