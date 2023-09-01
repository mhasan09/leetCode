# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        q = []
        return_list = []
        q.append(root)
        while len(q) > 0:
            level_data = []
            l = len(q)
            for i in range(l):
                current_data = q.pop(0)
                level_data.append(current_data.val)
                if current_data.left is not None:
                    q.append(current_data.left)
                if current_data.right is not None:
                    q.append(current_data.right)
            return_list.append(level_data)
        return return_list
