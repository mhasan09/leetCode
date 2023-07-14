# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        return self.get_height(root) != -1

    def get_height(self, root):
        if root is None:
            return 0

        left_height, right_height = self.get_height(root.left), self.get_height(root.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
