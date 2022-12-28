class Solution(object):
    def decodeString(self, s):
        current_string = ""
        stack = []
        current_number = 0
        for i in s:
            if i.isdigit():
                current_number = current_number*10 + int(i)
            elif i == "[":
                stack.append(current_string)
                stack.append(current_number)
                current_string = ""
                current_number = 0
            elif i == "]":
                num = stack.pop()
                previous_string = stack.pop()
                current_string = previous_string + num*current_string
            else:
                current_string += i
        return current_string

print(Solution().decodeString("3[a]2[bc]"))

