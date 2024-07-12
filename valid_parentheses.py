import collections


class Solution:
    def isValid(self, s: str) -> bool:
        data = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for i in s:
            if i in data:
                stack.append(i)
            else:
                if len(stack) != 0:
                    if data[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False


print(Solution().isValid("()"))
print(Solution().isValid("(())]]"))
print(Solution().isValid("(]"))
print(Solution().isValid("["))
