class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean

    '''
    Binary search of target on row
    '''
    def binarySearch(self, row, target):
    	length = len(row)
    	if length == 1:
    		if row[0] == target:
    			return True
    		else:
    			return False

    	mid = length // 2
    	if target == row[mid]:
    		return True
    	elif target < row[mid]:
    		return self.binarySearch(row[:mid],target)
    	else:
    		return self.binarySearch(row[mid:],target)


    def searchMatrix(self, matrix, target):
    	if len(matrix) == 0:
    		return False

    	for row in matrix:
    		if len(row) == 0:
    			return False
    		if target <= row[len(row)-1]:
    			return self.binarySearch(row,target)
    	return False


A = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
	]

sol = Solution()
print sol.searchMatrix([[1]],5)
# print sol.binarySearch(A[1],13)