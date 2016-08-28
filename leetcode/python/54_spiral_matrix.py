'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        if isinstance(matrix[0], int):
            return matrix

        row_start = 0
        row_end = len(matrix) - 1
        col_start = 0
        col_end = len(matrix[0]) - 1

        status = 0

        res = []

        while True:
            if row_start > row_end or col_start > col_end:
                break
            if status == 0:
                for col_index in range(col_start, col_end + 1):
                    res.append(matrix[row_start][col_index])
                row_start += 1
            elif status == 1:
                for row_index in range(row_start, row_end + 1):
                    res.append(matrix[row_index][col_end])
                col_end -= 1
            elif status == 2:
                for col_index in reversed(range(col_start, col_end+1)):
                    res.append(matrix[row_end][col_index])
                row_end -= 1
            elif status == 3:
                for row_index in reversed(range(row_start, row_end + 1)):
                    res.append(matrix[row_index][col_start])
                col_start += 1
            status = (status + 1) % 4

        return res

sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print sol.spiralOrder(matrix)

print sol.spiralOrder([])
print sol.spiralOrder([1])


