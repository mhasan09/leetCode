from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        data = []

        def calculate_partition(index):
            if index == len(s):
                answer.append(data.copy())
                return

            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    data.append(s[index: i + 1])
                    calculate_partition(i + 1)
                    data.pop()

        def isPalindrome(s, start, end):
            return s[start: end + 1] == s[start: end + 1][::-1]

        calculate_partition(0)
        return answer


print(Solution().partition("aabb"))
