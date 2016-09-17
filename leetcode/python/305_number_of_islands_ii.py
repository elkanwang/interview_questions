# class Node(object):
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.parent = None
#
#     def set_parent(self, node):
#         self.parent = node
#
#     def find(self):
#         '''
#         return the origin
#
#         :return:
#         '''
#         cur_node = self
#         while cur_node.parent:
#             cur_node = cur_node.parent
#         return cur_node
#
#     def union(self, node):
#         '''
#         union the two sets of nodes
#         :param node:
#         :return:
#         '''
#         find_self = self.find()
#         find_other = node.find()
#         find_other.set_parent(find_self)
#
# class Solution(object):
#     def numIslands2(self, m, n, positions):
#         """
#         :type m: int
#         :type n: int
#         :type positions: List[List[int]]
#         :rtype: List[int]
#         """
#         node_dict = {}
#         res_arr = []
#         cur_count = 0
#         for position_x, position_y in positions:
#             if (position_x, position_y) in node_dict:
#                 res_arr.append(cur_count)
#             nodes = set()
#             for x_offset, y_offset in [(0,1), (1,0), (0,-1), (-1,0)]:
#                 new_x = position_x + x_offset
#                 new_y = position_y + y_offset
#                 if 0 <= new_x < m and 0 <= new_y < n:
#                     if (new_x, new_y) in node_dict:
#                         nodes.add(node_dict[(new_x, new_y)].find())
#             new_node = Node(position_x, position_y)
#             node_dict[(position_x, position_y)] = new_node
#             if not nodes:
#                 cur_count += 1
#                 res_arr.append(cur_count)
#                 continue
#             else:
#                 nodes_len = len(nodes)
#                 cur_count -= nodes_len - 1
#                 res_arr.append(cur_count)
#                 parent = new_node
#                 for node in nodes:
#                     parent.union(node)
#                 continue
#         return res_arr
#


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent, rank, count = {}, {}, [0]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            # print x, y, rank[x], rank[y]
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                parent[y] = x
                rank[x] += int(rank[y] == rank[x])
                count[0] -= 1
            # print 'after: ', x, y, rank[x], rank[y], int(rank[x] == rank[y])

        def add((i, j)):
            x = parent[x] = i, j
            rank[x] = 0
            count[0] += 1
            for y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if y in parent:
                    union(x, y)
            return count[0]

        return map(add, positions)

sol = Solution()
print sol.numIslands2(3, 3, [[0,0],[0,1],[1,2],[2,1], [1,1]])
print sol.numIslands2(3, 3, [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])
