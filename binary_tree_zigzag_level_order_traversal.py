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
        if root is None:
            return root
        q = []
        return_list = []
        q.append(root)
        while len(q) > 0:
            level_data = []
            l = len(q)
            for i in range(l):
                current_data = q.pop(0)
                level_data.append(current_data.val)
                if current_data.left is not None:
                    q.append(current_data.left)
                if current_data.right is not None:
                    q.append(current_data.right)
            return_list.append(level_data)

        for i in range(len(return_list)):
            if i % 2 != 0:
                return_list[i] = return_list[i][::-1]
        return return_list

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left = node8
node4.right = node9

node6.left = node10
node7.right = node11
print(Solution().levelOrder(node1))