from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return root
        q = []
        result_data = []

        q.append(root)
        while len(q) > 0:
            current_sum = 0
            l = len(q)
            for _ in range(l):
                current_data = q.pop(0)
                current_sum += current_data.val
                if current_data.left is not None:
                    q.append(current_data.left)
                if current_data.right is not None:
                    q.append(current_data.right)

            result_data.append(current_sum/l)
        return result_data


"""
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
        return return_list

"""