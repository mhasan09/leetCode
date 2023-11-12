class Solution:
    def nextPermutation(self, arr):
        index = None

        for i in reversed(range(1,len(arr))):
            if arr[i] > arr[i-1]:
                index = i-1
                break

        if not index:
            return arr[::-1]

        for i in reversed(range(index, len(arr))):
            if arr[index] < arr[i]:
                arr[index], arr[i] = arr[i], arr[index]
                break

        return arr[:index+1]+arr[index+1:][::-1]


# print(Solution().nextPermutation([2, 1, 5, 4, 3, 0, 0]))
print(Solution().nextPermutation([3,2,1]))

