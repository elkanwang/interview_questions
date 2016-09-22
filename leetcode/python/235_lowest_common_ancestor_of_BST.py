# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p:
            return p
        if root == q:
            return q
        res_left = self.lowestCommonAncestor(root.left, p, q)
        res_right = self.lowestCommonAncestor(root.right, p, q)
        if (res_left == p and res_right == q) or (res_left == q and res_right == p):
            return root
        if not res_left:
            return res_right
        if not res_right:
            return res_left


t1 = TreeNode(1)
t2 = TreeNode(2)
t2.left = t1
sol = Solution()
sol.lowestCommonAncestor(t1, t2)