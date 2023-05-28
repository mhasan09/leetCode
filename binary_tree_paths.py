# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, path):
            if not node:
                return
            path = path + [node.val]
            if not (node.left or node.right):
                return paths.append(path)
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, [])
        return ['->'.join(map(str, path)) for path in paths]