class Solution:
    def isHappy(self, n: int):
        hash_set = set()

        while n != 1:
            if n in hash_set:
                return False

            hash_set.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True





print(Solution().isHappy(203))