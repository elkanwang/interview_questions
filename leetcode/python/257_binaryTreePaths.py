'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(node, s, d):
            if not node:
                return
            if len(s) > 0:
                s += "->" + str(node.val)
            else:
                s = str(node.val)
            if (not node.left) and (not node.right):
                d.add(s)
                return
            helper(node.left, s, d)
            helper(node.right, s, d)
            return
        d = set()
        helper(root, "", d)
        d = filter(lambda x: x!= "", list(d))
        return list(d)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
# t1.right = t3
sol = Solution()
print sol.binaryTreePaths(t1)
