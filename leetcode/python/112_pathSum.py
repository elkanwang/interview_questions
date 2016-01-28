# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        return bool( root and ( (root.left==root.right==None and root.val==sum) or (root.left and self.hasPathSum(root.left, sum-root.val) or (root.right and self.hasPathSum(root.right, sum-root.val) )

node = TreeNode(1)
node.right = TreeNode(2)
sol = Solution()
print sol.hasPathSum(None, 1)