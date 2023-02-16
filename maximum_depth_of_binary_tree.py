from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


'''
         10
       /    \
     5      19
           /
         17


# self. maxDepth(None) = 0 by definition

self. maxDepth(10)

max(self. maxDepth(5), self. maxDepth(19)) + 1 # First recursive call from node 10

max(max(self. maxDepth(None), self. maxDepth(None)) + 1, self. maxDepth(19)) + 1  # Recursive call on node 5 and its expansion

max(1, self. maxDepth(19)) + 1 # Replacing for self. maxDepth(None) = 0 

max(1, max(self. maxDepth(17), self. maxDepth(None)) + 1) + 1 # Recursive call from node 19

max(1, max(self. maxDepth(17), 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0 

max(1, max(max(self. maxDepth(None), self. maxDepth(None)) + 1, 0) + 1) + 1 # Recursive call from node 17

max(1, max(max(0, 0) + 1, 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0

max(1, max(0 + 1, 0) + 1) + 1 # Replacing the inner most max

max(1, 1 + 1) + 1 # Replacing the inner most max

max(1, 2) + 1

2 + 1 # Replacing the inner most max

3

'''