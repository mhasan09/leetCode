# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.helper(root)
        return self.max_diameter

    def helper(self, root):
        if root is None:
            return 0

        left_depth = self.helper(root.left)
        right_depth = self.helper(root.right)

        current_diameter = left_depth + right_depth
        self.max_diameter = max(self.max_diameter, current_diameter)

        return 1 + max(left_depth, right_depth)