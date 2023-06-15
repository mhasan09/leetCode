import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        level = 0
        ans = 0

        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            current_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                print(node.val)
                current_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                ans = level

        return ans
