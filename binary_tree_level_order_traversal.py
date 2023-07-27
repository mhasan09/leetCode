# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        return_list = []
        queue = deque()
        queue.append([root])

        while queue:
            ans = []
            for i in range(len(queue)):
                node = queue.popleft()
                ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            return_list.append(ans)

        return return_list