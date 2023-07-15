# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum_path_sum = 0
        self.helper(root)
        return self.maximum_path_sum

    def helper(self, root):
        if root is None:
            return 0

        left_subtree_sum = max(0, self.helper(root.left))
        right_subtree_sum = max(0, self.helper(root.right))

        current_sum = left_subtree_sum + right_subtree_sum + root.val

        self.maximum_path_sum = max(current_sum, self.maximum_path_sum)

        return root.val + max(left_subtree_sum, right_subtree_sum)