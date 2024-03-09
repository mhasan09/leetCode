class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = []
        s = ""
        for i in range(1, n + 1):
            s += f"{i}"

        self.calculate_permutation(s=s, index=0, answer=answer)
        answer.sort()
        return answer[k - 1]

    def calculate_permutation(self, s, index, answer):
        if index == len(s):
            answer.append(s)
            return

        for i in range(index, len(s)):
            s = self.swap(s, index, i)
            self.calculate_permutation(s, index + 1, answer)
            s = self.swap(s, index, i)

    @staticmethod
    def swap(s, val_1, val_2):
        s = list(s)
        s[val_1], s[val_2] = s[val_2], s[val_1]
        return "".join(s)


# print(Solution().getPermutation(3, 3))


class OptimizedSolution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = ""
        factorial = 1
        data = []
        for i in range(1, n):
            factorial *= i
            data.append(i)
        data.append(n)
        k -= 1
        while True:
            answer += str(data[k // factorial])
            data.pop(k // factorial)
            if not data:
                break
            k %= factorial
            factorial //= len(data)
        return answer


print(OptimizedSolution().getPermutation(4, 3))
