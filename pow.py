class Solution:
    def myPow(self, number: float, power: int) -> float:
        answer = 1.0
        p = power

        if p < 0:
            p = -1 * p

        while p:
            if p % 2 == 0:
                number = number * number
                p = p // 2

            else:
                answer = answer * number
                p = p - 1

        if power < 0:
            answer = 1.0 / answer

        return answer


# print(Solution().myPow(2.0000, 10))
print(Solution().myPow(2.0000, -2))

