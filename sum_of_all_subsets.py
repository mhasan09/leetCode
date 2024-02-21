class Solution:
    def subsetSums(self, arr):
        result = []

        def calculate_subset_sum(index, current_sum):
            if index == len(arr):
                result.append(current_sum)
                return
            calculate_subset_sum(index + 1, current_sum + arr[index])
            calculate_subset_sum(index + 1, current_sum)

        calculate_subset_sum(0, 0)
        result.sort()
        return result

print(Solution().subsetSums([3, 1, 2]))
