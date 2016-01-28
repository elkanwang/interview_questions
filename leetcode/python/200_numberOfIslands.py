# count the # of cell that has no neighours on top of it and at the left of it

class Solution:
	def isIsland(self, grid, i, j):
		# print 'i: ',i, ' j: ',j, '  ', grid[i][j]
		if i < 0 or j < 0 or grid[i][j] != '1':
			return True

    # @param grid, a list of list of characters
    # @return an integer
	def numIslands(self, grid):
		if len(grid) == 0:
			return 0
		if len(grid) == 1:
			return 1 if grid[0] == '1' else 0
		m = len(grid)
		n = len(grid[0])
		count = 0
		for i in range(m):
			for j in range(n):
				if self.isIsland(grid, i-1, j) and self.isIsland(grid, i, j-1):
					count += 1
		return count



# class Solution:
#     def visit(self, grid, m, n, i, j):
#         if (i<0 or j<0 or i>m or j>n or grid[i][j]!='1'):
#             return False
#         grid[i]= 'v'
#         self.visit(grid, m, n, i+1, j)
#         self.visit(grid, m, n, i-1, j)
#         self.visit(grid, m, n, i, j+1)
#         self.visit(grid, m, n, i, j-1)
#         return True
#     # @param {character[][]} grid
#     # @return {integer}
#     def numIslands(self, grid):
#         if len(grid)==0:
#             return 0
#         m = len(grid)
#         n = len(grid[0])
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 count += 1 if self.visit(grid, m, n, i, j) else 0
#         return count

sol = Solution()
print sol.numIslands(["1"])