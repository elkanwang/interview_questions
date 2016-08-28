'''
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

Proposed method:

1. use trie
2. dfs

'''

#
# from collections import OrderedDict
# class Node(object):
#
#     def __init__(self, val):
#         self.val = val
#         self.children = OrderedDict()
#         self.terminate = False
#
#     def insert(self, number_str):
#         if not number_str:
#             return
#         char, rest  = number_str[0], number_str[1:]
#         if char in self.children:
#             if not rest:
#                 self.children[char].terminate = True
#             else:
#                 self.children[char].insert(rest)
#         else:
#             new_node = Node(char)
#             if not rest:
#                 new_node.terminate = True
#             else:
#                 new_node.insert(rest)
#             self.children[char] = new_node
#
#
# class Solution(object):
#     def lexicalOrder(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         root = Node('')
#         for i in range(1, n+1):
#             root.insert(str(i))
#
#         def print_tree(node, sofar, arr):
#             if node.terminate:
#                 arr.append(int(sofar+node.val))
#             for char, child in node.children.iteritems():
#                 print_tree(child, sofar+node.val, arr)
#         res = []
#         print_tree(root, '', res)
#         return res
#
# sol = Solution()
# print sol.lexicalOrder(100)


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        sofar = 0
        res = []
        def helper(sofar, arr):
            for i in range(10):
                new_sofar = sofar * 10 + i
                if new_sofar == 0:
                    continue
                if new_sofar <= n:
                    arr.append(new_sofar)
                    helper(new_sofar, arr)
                else:
                    break
        helper(sofar, res)
        return res
sol = Solution()
print sol.lexicalOrder(23489)

