# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def inorder_traversal(root):
            if root:
                inorder_traversal(root.left)
                arr.append(root.val)
                inorder_traversal(root.right)

        inorder_traversal(root)

        new_tree = TreeNode(val=arr[0])

        # Use a marker to track our tree location in memory.
        temp = new_tree

        # Iterate through our vals, creating a new right node with the current val.
        for i in arr[1:]:
            temp.right = TreeNode(val=i)

            # Move the marker to the next node.
            temp = temp.right

        return new_tree
