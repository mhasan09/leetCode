"""
# Definition for a Node.
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, ans = [root], []
        while len(stack):
            top = stack.pop()
            ans.append(top.val)
            stack.extend(reversed(top.children))
        return ans
