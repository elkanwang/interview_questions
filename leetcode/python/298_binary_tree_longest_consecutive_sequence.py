# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, val = self.helper(root)
        return val

    def helper(self, root):
        if not root:
            return [], 0

        left_res = self.helper(root.left)
        right_res = self.helper(root.right)

        # print 'left', left_res
        # print 'right', right_res
        # print 'root', root.val
        if left_res[1] == 0 and right_res[1] == 0:
            return [root.val], 1
        sofar_left = left_res[0]
        sofar_right = right_res[0]
        arr_left, arr_right = None, None
        if sofar_left:
            if len(sofar_left) >= 1 and sofar_left[-1] - root.val == 1:
                arr_left = sofar_left + [root.val]
            else:
                arr_left = [root.val]
        else:
            arr_left = [root.val]
        if sofar_right:
            # print 'right', 'sofar_right', sofar_right, 'root val', root.val
            if len(sofar_right) >= 1 and sofar_right[-1] - root.val == 1:
                arr_right = sofar_right + [root.val]
            else:
                arr_right = [root.val]
        else:
            arr_right = [root.val]
        sofar_arr = arr_left if len(arr_left) > len(arr_right) else arr_right
        sofar_max = max(len(sofar_arr), left_res[1], right_res[1])
        # print 'root', root.val, sofar_left, sofar_right, sofar_arr, 'max of', len(sofar_arr), left_res[1], right_res[1]
        return sofar_arr, sofar_max

