# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        if not root:
            return False

        def dfs(node, path):
            if not node.left and not node.right:
                path += [node.val]
                res.append(path)

            if node.left:
                dfs(node.left, path + [node.val])

            if node.right:
                dfs(node.right, path + [node.val])

        dfs(root, [])
        for arr in res:
            if sum(arr) == targetSum:
                return True
        return False
