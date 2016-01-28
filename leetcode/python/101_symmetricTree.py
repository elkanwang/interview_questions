# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        res = []
        self.gen(root, res, 0)
        for i in range(len(res)):
            if self.isSym(res[i]) == False:
                return False
        return True
        
    def gen(self, root, res=[], curDepth=0):
        if not root:
            if len(res) == curDepth:
                res.append([0])
            else:
                res[curDepth].append(0)
            return
        if len(res) == curDepth:
            res.append([root.val])
        else:
            res[curDepth].append(root.val)
        self.gen(root.left, res, curDepth+1)
        self.gen(root.right, res, curDepth+1)
        
    def isSym(self, array):
        if array == [] or len(array)==1:
            return True
        if array[0] == array[-1]:
            return self.isSym(array[1:-1])
        else:
            return False
    
node1 = TreeNode(1)
node2 = TreeNode(2)
node1.right = node2
sol = Solution()
print sol.isSymmetric(node1)
