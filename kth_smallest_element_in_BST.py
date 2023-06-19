from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        data = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            data.append(root.val)
            inorder(root.right)
        inorder(root)

        if k > len(data):
            return -1

        return data[k-1]