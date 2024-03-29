from typing import List


class Solution:
    def isAlienSorted(self, W: List[str], O: str) -> bool:
        alpha = {O[i]: i for i in range(len(O))}
        for i in range(1,len(W)):
            a, b = W[i-1], W[i]
            for j in range(len(a)):
                if j == len(b): return False
                first, second = a[j], b[j]
                aix, bix = alpha[first], alpha[second]
                if aix < bix: break
                if aix > bix: return False
        return True


print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
