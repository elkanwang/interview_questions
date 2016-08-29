# # count the # of cell that has no neighours on top of it and at the left of it
#
# class Solution:
# 	def isIsland(self, grid, i, j):
# 		# print 'i: ',i, ' j: ',j, '  ', grid[i][j]
# 		if i < 0 or j < 0 or grid[i][j] != '1':
# 			return True
#
#     # @param grid, a list of list of characters
#     # @return an integer
# 	def numIslands(self, grid):
# 		if len(grid) == 0:
# 			return 0
# 		if len(grid) == 1:
# 			return 1 if grid[0] == '1' else 0
# 		m = len(grid)
# 		n = len(grid[0])
# 		count = 0
# 		for i in range(m):
# 			for j in range(n):
# 				if self.isIsland(grid, i-1, j) and self.isIsland(grid, i, j-1):
# 					count += 1
# 		return count



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
#
# sol = Solution()
# print sol.numIslands(["1"])
import Queue

class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        proposed solution: BFS
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0
        width = len(grid)
        height = len(grid[0])
        def helper(grid, start_x, start_y, width, height):
            queue = Queue.Queue()
            queue.put((start_x, start_y))
            while not queue.empty():
                x, y = queue.get()
                if grid[x][y] == '0':
                    continue
                grid[x] = grid[x][:y] + '0' + grid[x][y+1:]
                if (x-1) >= 0 and grid[x-1][y] == '1':
                    queue.put((x-1, y))
                if (x+1) < width and grid[x+1][y] == '1':
                    queue.put((x+1, y))
                if (y-1) >= 0 and grid[x][y-1] == '1':
                    queue.put((x, y-1))
                if (y+1) < height and grid[x][y+1] == '1':
                    queue.put((x, y+1))
                print x, y, queue.qsize(), grid
            return grid
        res = 0
        for i in range(width):
            for j in range(height):
                if grid[i][j] == '1':
                    res += 1
                    grid = helper(grid, i, j, width, height)
        return res


sol = Solution()
grid = ["11110","11010","11000","00000"]
grid_2 = ["11000", "11000", "00100", "00011"]
grid_3 = ["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]
print sol.numIslands(grid)
print sol.numIslands(grid_2)
print sol.numIslands(grid_3)