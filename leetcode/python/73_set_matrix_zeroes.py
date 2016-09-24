class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m = len(matrix)
        n = len(matrix[0])

        def switch(i, j, m, n):
            for x in range(m):
                matrix[x][j] &= 2
            for y in range(n):
                matrix[i][y] &= 2

        for i in range(m):
            for j in range(n):
                matrix[i][j] += (matrix[i][j] < 1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] & 2:
                    switch(i, j, m, n)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] & 2:
                    matrix[i][j] >= 1

        return