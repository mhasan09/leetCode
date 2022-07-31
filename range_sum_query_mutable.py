class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.BIT = [0] * (len(self.nums) + 1)
        for i in range(len(self.nums)):
            self.update(i, nums[i], True)

    def update(self, i: int, val: int, init=False) -> None:
        if not init:
            # only update the difference
            val, self.nums[i] = val - self.nums[i], val
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += val
            i += (i & -i)

    def sumRange(self, i: int, j: int) -> int:
        return self.query(j) - self.query(i - 1)

    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.BIT[i]
            i -= (i & -i)
        return ans