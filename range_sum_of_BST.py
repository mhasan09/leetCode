# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                if low <= root.val <= high:
                    arr.append(root.val)
                inorder_traversal(root.right)
        inorder_traversal(root)
        return sum(arr)