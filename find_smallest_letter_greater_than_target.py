from typing import List


class Solution:
    def check_same_element(self, arr):
        if len(set(arr)) == 1:
            return True
        else:
            first_element = arr[0]
            for i in arr:
                if i is not first_element:
                    return i

    def nextGreatestLetter(self, arr: List[str], target: str) -> str:
        if target == "z":
            return arr[0]
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > arr[m]:
                l = m + 1
            elif target < arr[m]:
                r = m - 1
            else:
                data = self.check_same_element(arr[m:])
                if data is True:
                    return arr[0]
                else:
                    return data


        if l > len(arr) - 1:
            return arr[0]
        else:
            return arr[l]


# print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))
print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))
# print(Solution().nextGreatestLetter(["c", "f", "j"], "d"))
# print(Solution().nextGreatestLetter(["c", "f", "j"], "k"))
# print(Solution().nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], "e"))
# print(Solution().nextGreatestLetter(["x", "x", "y", "y"], "y"))
