class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestorofBT(self, root, p, q):
        if not root or (root == p) or (root == q):
            return root

        left = self.lowestCommonAncestorofBT(root.left, p, q)
        right = self.lowestCommonAncestorofBT(root.right, p, q)

        if left and right:
            return root

        return left or right
