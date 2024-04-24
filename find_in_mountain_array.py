# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
        finding the peak of the mountain array first
        """
        low, high = 0, mountain_arr.length() - 1
        max_index = 0
        while low < high:
            mid = low + (high - low) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                low = mid + 1
            else:
                high = mid

        """
        re-evaluate the peak to search at the left side 
        """
        max_index = low
        low = 0
        high = max_index

        while low <= high:
            mid = low + (high - low) // 2
            data = mountain_arr.get(mid)
            if data < target:
                low = mid + 1
            elif data > target:
                high = mid - 1
            else:
                return mid

        """
        re-evaluate the peak to search at the right side 
        """
        low = max_index
        high = mountain_arr.length() - 1
        while low <= high:
            mid = low + (high - low) // 2
            data = mountain_arr.get(mid)
            if data > target:
                low = mid + 1
            elif data < target:
                high = mid - 1
            else:
                return mid
        return -1



print(Solution().findInMountainArray(3, [1, 2, 3, 4, 5, 3, 1]))
print(Solution().findInMountainArray(3, [0,1,2,4,2,1]))
