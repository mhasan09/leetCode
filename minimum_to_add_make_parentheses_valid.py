class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        counter = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif stack and stack[-1] == "(" and i == ")":
                stack.pop()
            else:
                counter += 1
        return counter + len(stack)


print(Solution().minAddToMakeValid("())"))
print(Solution().minAddToMakeValid("((("))