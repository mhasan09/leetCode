# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        ans = []
        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                data.append(root.val)
                inorder_traversal(root.right)

        inorder_traversal(root)
        data = collections.Counter(data)
        max_val = max(data.values())
        for k,v in data.items():
            if v == max_val:
                ans.append(k)
        return ans