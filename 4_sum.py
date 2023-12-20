from typing import List


class Solution:
    def fourSum(self, arr: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(arr)
        arr.sort()

        for i in range(n):
            # avoid the duplicates while moving i:
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n):
                # avoid the duplicates while moving j:
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                k = j + 1
                l = len(arr) - 1

                while k < l:
                    current_sum = arr[i] + arr[j] + arr[k] + arr[l]
                    if current_sum == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        answer.append(temp)

                        k += 1
                        l -= 1

                        while k < l and arr[k] == arr[k - 1]:
                            k += 1
                        while k < l and arr[l] == arr[l + 1]:
                            l -= 1

                    elif current_sum < target:
                        k += 1
                    else:
                        l -= 1
        return answer



# print(Solution().fourSum([1,0,-1,0,-2,2], 0))
print(Solution().fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4))
