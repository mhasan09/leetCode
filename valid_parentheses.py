import collections


class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []
        for i in s:

            if i in data:
                stack.append(i)

            elif len(stack) == 0 or data[stack.pop()] != i:
                return False

        return len(s) == 0




print(Solution().isValid("()[]{}"))
# print(Solution().isValid("(]"))
