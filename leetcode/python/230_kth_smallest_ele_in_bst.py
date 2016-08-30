# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def helper(root, k, res):
            if root is None:
                return k, res
            k, res = helper(root.left, k, res)


            if res is not None:
                pass
            elif k == 1:
                res = root.val
                # print res
            else:
                k -= 1
            # print k, res
            k, res = helper(root.right, k, res)
            return k, res


        _, res = helper(root, k, None)
        return res

t1 = TreeNode(0)
t2 = TreeNode(2)
t3 = TreeNode(1)
t1.right = t2
t2.left = t3
sol = Solution()
print sol.kthSmallest(t1, 2)