# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root, min, max):
            if not root:
                return True
            left_bool = helper(root.left, min, root.val)
            right_bool= helper(root.right, root.val, max)
            if not (left_bool and right_bool):
                return False
            if min is None and max is None:
                return True
            elif min is None:
                return root.val < max
            elif max is None:
                return root.val > min
            else:
                return min < root.val < max
        return helper(root, None, None)

    # method 2: use in-order traversal