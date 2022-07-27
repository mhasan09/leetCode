# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#  root = [1,2,5,3,4,null,6]
#  output = [1,null,2,null,3,null,4,null,5,null,6]



class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        current = root
        while current:
            if current.left:
                left = current.left  # get the left subtree of current
                right = current.right  # get the right subtree of current
                current.left = None  # current's left subtree set to be None
                current.right = left  # switch the left subtree to the right subtree
                while left.right:  # get the far-right leaf of the left subtree
                    left = left.right
                left.right = right  # put the right subtree of current as the right subtree of the far-right leaf
            current = current.right  # go down the right direction



