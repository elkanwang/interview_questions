'''
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary
tree. You do not necessarily need to follow this format, so please be creative
and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t5 = TreeNode(5)
t4 = TreeNode(4)
t3 = TreeNode(3)
t3.left = t4
t3.right = t5
t2 = TreeNode(2)
t1 = TreeNode(1)
t1.left = t2
t1.right = t3

# class Codec:

    # def serialize(self, root):
        # """Encodes a tree to a single string.

        # :type root: TreeNode
        # :rtype: str
        # """

        # import Queue
        # stack = Queue.Queue()
        # stack.put(root)
        # result = ''
        # while not stack.empty():
            # p = stack.get()
            # if p:
                # result += str(p.val) + ','
                # stack.put(p.left)
                # stack.put(p.right)
            # else:
                # result += "None,"
        # return result

    # def deserialize(self, data):
        # """Decodes your encoded data to tree.

        # :type data: str
        # :rtype: TreeNode
        # """
        # data = data.split(',')
        # print data
        # if len(data)<=2:
            # return None
        # if data[0] == 'None':
            # return None
        # t = TreeNode(int(data[0]))
        # import Queue
        # stack = Queue.Queue()
        # stack.put(t)
        # while not stack.empty():
            # p = stack.get()
            # data = data[1:]
            # if data[0] != 'None':
                # temp = TreeNode(int(data[0]))
                # stack.put(temp)
                # p.left = temp
                # data = data[1:]
            # if data[0] != 'None':
                # temp = TreeNode(int(data[0]))
                # stack.put(temp)
                # p.right = temp
                # data = data[1:]
        # return t

class Codec(object):
    def serialize(self, root):
        def helper(node):
            if not node:
                vals.append('null')
                return
            vals.append(str(node.val))
            helper(node.left)
            helper(node.right)
        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == 'null':
                return None
            else:
                node = TreeNode(int(val))
                node.left = helper()
                node.right = helper()
                return node

        vals = iter(data.split())
        return helper()





# Your Codec object will be instantiated and called as such:
codec = Codec()
print codec.serialize(t5)
print codec.serialize(codec.deserialize(codec.serialize(t5)))
print codec.serialize(t5)
# codec.deserialize(codec.serialize(root))
