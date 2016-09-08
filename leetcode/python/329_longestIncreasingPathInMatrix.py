#
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move
# outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if (not matrix) or (not matrix[0]):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res_arr = []
        for i in range(m):
            for j in range(n):
                res_arr.append(self.fromCell(matrix, i, j, m, n))
        return max(res_arr)

    def fromCell(self, matrix, x, y, m, n):
        # print x, y, matrix
        value = matrix[x][y]
        res_arr = []
        matrix[x][y] = None
        for inc_x, inc_y in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_x, new_y = x+inc_x, y+inc_y
            if 0<=new_x<m and 0<=new_y<n and (matrix[new_x][new_y] is not None) and matrix[new_x][new_y] > value:
                res_arr.append(self.fromCell(matrix, new_x, new_y, m, n))
        matrix[x][y] = value
        if not res_arr:
            return 1
        else:
            return 1 + max(res_arr)

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

nums2 = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

sol = Solution()
print sol.longestIncreasingPath(nums)
print sol.longestIncreasingPath(nums2)