class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        for i in s:
            if i != "#":
                stack_s.append(i)
            else:
                if len(stack_s) != 0:
                    stack_s.append("#")
                    stack_s.pop()
                    stack_s.pop()
        for i in t:
            if i != "#":
                stack_t.append(i)
            else:
                if len(stack_t) != 0:
                    stack_t.append("#")
                    stack_t.pop()
                    stack_t.pop()
        return stack_s == stack_t



print(Solution().backspaceCompare("ab#c", "ad#c"))
print(Solution().backspaceCompare("ab##", "c#d#"))
print(Solution().backspaceCompare("a#c", "b"))
print(Solution().backspaceCompare("a##c", "b"))
