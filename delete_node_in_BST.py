from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # leaf node
            if not root.left and not root.right:
                root = None

            # 1 child only
            elif not root.left:
                root = root.right

            elif not root.right:
                root = root.left

            # 2 child
            else:
                # get the minimum value of right subtree and store in temp variable
                temp = self.find_min(root.right)
                root.val = temp.val

                # send it to the leaf node recursively
                root.right = self.deleteNode(root.right, temp.val)

        return root
