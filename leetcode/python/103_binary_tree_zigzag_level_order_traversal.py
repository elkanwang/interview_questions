# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        direction = 0
        res = []
        while stack:
            cur_level = []
            next_level = []
            for item in reversed(stack):
                cur_level.append(item.val)
                if direction == 0:
                    if item.left:
                        next_level.append(item.left)
                    if item.right:
                        next_level.append(item.right)
                else:
                    if item.right:
                        next_level.append(item.right)
                    if item.left:
                        next_level.append(item.left)
            stack = next_level
            direction = (direction + 1) % 2
            res.append(cur_level)
        return res

