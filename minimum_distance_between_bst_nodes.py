from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        data = []

        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            data.append(root.val)
            inorder(root.right)

        inorder(root)

        min_dist = 100000000

        for i in range(1, len(data)):
            dist = data[i] - data[i-1]
            min_dist = min(min_dist, dist)

        return min_dist