class Solution:
    def minInsertions(self, s: str) -> int:
        ret = 0
        s = s.replace('))', ']')
        ret += s.count(')')
        s = s.replace(')', ']')
        bal = 0
        for i, v in enumerate(s):
            if v == '(':
                bal += 1
            elif v == ']':
                bal -= 1
            if bal == -1:
                ret += 1
                bal += 1
        return ret + 2 * bal

print(Solution().minInsertions("(()))"))
print(Solution().minInsertions(")())("))
