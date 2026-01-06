import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float("-inf"), 0, 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            level += 1
            sum_at_current_level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum_at_current_level += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if sum_at_current_level > max_sum:
                max_sum = sum_at_current_level
                ans = level
        return ans