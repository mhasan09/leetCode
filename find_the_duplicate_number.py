from typing import List

"""
This is a fast and slow pointer approach, if the array
contains duplicate element then it'll form a cycle 
We'll iterate the fast and slow pointer until slow == fast 


"""

class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        slow = arr[0]
        fast = arr[0]
        while True:
            slow = arr[slow]
            fast = arr[arr[fast]]
            if slow == fast:
                break
        fast = arr[0]
        while slow != fast:
            slow = arr[slow]
            fast = arr[fast]
        return slow


print(Solution().findDuplicate([1,3,4,2,3]))