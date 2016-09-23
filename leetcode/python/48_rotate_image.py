class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        /*
         * clockwise rotate
         * first reverse up to down, then swap the symmetry
         * 1 2 3     7 8 9     7 4 1
         * 4 5 6  => 4 5 6  => 8 5 2
         * 7 8 9     1 2 3     9 6 3
        */
        """

        def helper(matrix, i, j):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        matrix = matrix[::-1]
        for i in range(n):
            for j in range(i, n):
                helper(matrix, i, j)
        print matrix

sol = Solution()
sol.rotate([[1]])
sol.rotate([[1,2],[3,4]])