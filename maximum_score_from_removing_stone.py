class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = sorted([a, b, c])
        result = 0
        while len(stones) > 1:
            # remove from first and last pile in each iteration
            stones[0], stones[-1] = stones[0] - 1, stones[-1] - 1
            result += 1

            # check whether first pile is empty or not
            if stones[0] == 0:
                stones = stones[1:]

            # check whether last pile is empty or not
            if stones[-1] == 0:
                stones = stones[:-1]

            stones = sorted(stones)

        return result


# print(Solution().maximumScore(a=2, b=4, c=6))
print(Solution().maximumScore(a=4, b=4, c=6))
