# class Solution(object):
#     def calcEquation(self, equations, values, queries):
#         """
#         :type equations: List[List[str]]
#         :type values: List[float]
#         :type queries: List[List[str]]
#         :rtype: List[float]
#         """
#         variables = set()
#         eqns = set()
#         for i, (variable_x, variable_y) in enumerate(equations):
#             variables.add(variable_y)
#             variables.add(variable_x)
#             tmp = set()
#             tmp.add((variable_x, variable_y, values[i]))
#             tmp.add((variable_y, variable_x, 1.0 / values[i]))
#             for v1, v2, val in eqns:
#                 # print v1, v2, variable_x, variable_y
#                 if v2 == variable_x:
#                     tmp.add((v1, variable_y, values[i] * val))
#                     tmp.add((variable_y, v1, 1.0 / (values[i] * val)))
#                 if v2 == variable_y:
#                     tmp.add((v1, variable_x, 1.0 / (values[i]) * val))
#                     tmp.add((variable_x, v1, values[i] * (1.0 / val)))
#                 # print tmp
#             eqns |= tmp
#         res = []
#         # print eqns
#         for variable_x, variable_y in queries:
#             if (variable_x not in variables) or (variable_y not in variables):
#                 res.append(-1.0)
#             elif variable_x == variable_y:
#                 res.append(1.0)
#             else:
#                 equation = filter(lambda x: x[0] == variable_x and x[1] == variable_y, eqns)
#                 if not equation:
#                     res.append(-1.0)
#                 else:
#                     res.append(equation[0][2])
#         return res
# sol = Solution()
# sol.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
# sol.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])
# sol.calcEquation([["a","e"],["b","e"]], [4.0,3.0], [["a","b"],["e","e"],["x","x"],["b","a"]])


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]


        build a graph, and query can just try to follow the graph
        """
