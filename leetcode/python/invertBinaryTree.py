# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
    	if not root:
    		return root
    	# print root.val
    	temp = root.left
    	root.left = self.invertTree(root.right)
    	root.right = self.invertTree(temp)
    	return root

        
t1 = TreeNode(1)
print Solution().invertTree(t1)