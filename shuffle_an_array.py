import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums[:]

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        answer = self.arr[:]
        n = len(answer)
        for i in range(n):
            rand_data = random.randrange(i, n)
            answer[i], answer[rand_data] = answer[rand_data], answer[i]
        return answer


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()