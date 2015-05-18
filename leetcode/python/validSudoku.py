class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        for i in range(9):
        	if not self.isValid(board, 0, 9, i, i+1):
        		return False
        	if not self.isValid(board, i, i+1, 0, 9):
        		return False
        return self.isValid(board, 0, 3, 0, 3) and self.isValid(board, 0, 3, 3, 6) and self.isValid(board, 0, 3, 6, 9) and self.isValid(board, 3, 6, 0, 3) and self.isValid(board, 3, 6, 3, 6) and self.isValid(board, 3, 6, 6, 9) and self.isValid(board, 6, 9, 0, 3) and self.isValid(board, 6, 9, 3, 6) and self.isValid(board, 6, 9, 6, 9)


    def isValid(self, board, m1, m2, n1, n2):
    	sudokuDict = {x:0 for x in range(1,10)}
    	for i in range(m1, m2):
    		for j in range(n1, n2):
    			if board[i][j] == ".":
    				continue
    			elif sudokuDict[int(board[i][j])] != 0:
    				return False
    			else:
    				sudokuDict[int(board[i][j])] += 1
    	return True

a = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()
print sol.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])


#alternate solution
# class Solution:
#     # @param {character[][]} board
#     # @return {boolean}
#     def isValidSudoku(self, board):
#         if not board:
#             return False

#         row, col, box = [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)]

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 num = board[i][j]
#                 if num != '.':
#                     index = int(num) - 1
#                     k = i / 3 * 3 + j / 3
#                     if row[i][index] or col[j][index] or box[k][index]:
#                         return False

#                     row[i][index] = col[j][index] = box[k][index] = True

#         return True


# row, col, box are flags to check whether a number in a row/col/3x3box has been used before or not. e.g. row[0] represents the boolean flag for each 1-9 number of the first row, namely row[0][0] is boolean flag for 1, row[0][1] is for 2, etc.

# When we iterate through the board, we mark the current number as visited in each row, col, box. So the goal here is, in a valid board, all the numbers of 1-9 should only be used once in each row, col, box. Otherwise the board is invalid.

# As to the i, j - A simple way to make it clear for you is by drawing the board on a paper yourself, and let's say you are given i, j = 2, 3, how do you locate which 3x3box that element belongs to? k = i / 3 * 3 + j / 3 is used to calculate the 3x3box index that element belongs to.