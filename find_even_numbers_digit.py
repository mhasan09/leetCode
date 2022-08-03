class Solution:
    def findNumbers(self, arr):
        count = 0
        for i in arr:
            if self.len_of_a_num(i) % 2 == 0:
                count += 1
        return count

    def len_of_a_num(self, n):
        import math
        return int(math.log10(n)) + 1
