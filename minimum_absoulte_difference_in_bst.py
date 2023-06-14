# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        item = []

        def dfs(node):
            if node is None:
                return

            item.append(node.val)
            dfs(node.left)
            dfs(node.right)

        min_val = 1e9
        item.sort()
        for i in range(1, len(item)):
            min_val = min(min_val, item[i] - item[i-1])

        return min_val
