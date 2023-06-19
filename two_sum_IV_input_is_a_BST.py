from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        data = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            data.append(root.val)
            inorder(root.right)

        inorder(root)

        seen = set()
        for i in data:
            if (k-i) in seen:
                return True
            seen.add(i)
        return False
