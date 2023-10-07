class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for index,word in enumerate(s):
            s[index] = s[index][::-1]
        return " ".join(s)


print(Solution().reverseWords("God Ding"))
