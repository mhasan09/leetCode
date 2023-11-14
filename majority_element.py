class Solution:
    def majorityElement(self, nums):
        """ using moore's voting algorithm """
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


print(Solution().majorityElement([2, 2, 3, 3, 4, 4, 1, 1, 5]))
