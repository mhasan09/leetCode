from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = ["1", "2"]
        if n == 1:
            return ["1"]
        elif n == 2:
            return ["1", "2"]
        else:
            for i in range(3, n+1):
                if i % 3 == 0 and i % 5 == 0:
                    ans.append("FizzBuzz")
                elif i % 3 == 0:
                    ans.append("Fizz")
                elif i % 5 == 0:
                    ans.append("Buzz")
                else:
                    ans.append(str(i))
            return ans

print(Solution().fizzBuzz(3))
print(Solution().fizzBuzz(5))
print(Solution().fizzBuzz(15))