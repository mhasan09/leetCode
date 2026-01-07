# Definition for a binary tree node.
from typing import Optional

from subset_sum_equals_to_k import total_sum


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sum = []
        def tree_sum(node):
            if node is None:
                return 0
            left_side_sum = tree_sum(node.left)
            right_side_sum = tree_sum(node.right)

            current_sum = node.val + left_side_sum + right_side_sum
            all_sum.append(current_sum)
            return current_sum

        total_sum = tree_sum(root)
        best = 0
        for s in all_sum:
            current_product = s * (total_sum - s)
            best = max(best, current_product)

        return best % (10**9 + 7)
