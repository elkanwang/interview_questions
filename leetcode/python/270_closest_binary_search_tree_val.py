# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        def helper(root, target, prev):
            # print target, prev
            if not root:
                return prev
            if root.val == target:
                return root.val
            res = None
            if root.val < target:
                res = helper(root.right, target, root.val)
            elif root.val > target:
                res = helper(root.left, target, root.val)
            if abs(res - target) < abs(root.val - target):
                return res
            else:
                return root.val

        return helper(root, target, None)

t1 = TreeNode(1)
# t2 = TreeNode(1)
# t1.left = t2
sol = Solution()
print sol.closestValue(t1, 9.99)