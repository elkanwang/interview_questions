# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        if (self.depth(root.left) - self.depth(root.right)) not in range(-1,2):
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right))+1

node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1)
node1.right = node2
node2.left = node3

sol = Solution()
print sol.isBalanced(node1)