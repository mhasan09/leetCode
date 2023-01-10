from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if root:
            result.append(root.val)
            self.dfs(root.left, result)
            self.dfs(root.right, result)
