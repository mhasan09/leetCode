class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = 0
        max_right[n - 1] = 0

        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])

        output = 0

        for i in range(n):
            lower_boundary = min(max_left[i], max_right[i])
            max_trap_at_i = lower_boundary - height[i]
            if max_trap_at_i > 0:
                output += max_trap_at_i
        return output


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
