from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        index_of_inorder = {c: i for i, c in enumerate(inorder)}
        self.root_index = 0

        def helper(l, r):
            if l > r: return None
            root = TreeNode(preorder[self.root_index])
            self.root_index += 1

            i = index_of_inorder[root.val]
            root.left = helper(l, i - 1)
            root.right = helper(i + 1, r)
            return root

        return helper(0, len(preorder) - 1)