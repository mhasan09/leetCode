# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque()
        level_sums = []
        q.append(root)

        while q:
            current_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                current_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level_sums.append(current_sum)

        if len(level_sums) > k:
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]