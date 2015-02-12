class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
    	# get rid of non-positive elements
    	for n in A:
    		if n <= 0:
    			A.remove(n)
    	# if the list is empty, return 1
    	if A == []:
    		return 1

        maximum = max(A)
        res = [0] * maximum
        for n in A:
        	if n > 0:
        		res[n-1] = 1
        # find the hole, and report the first missing positive integer
        for i in range(len(res)):
        	if res[i] == 0:
        		return i + 1
        return maximum+1

sol = Solution()
A = [4,-1,1]
print sol.firstMissingPositive(A)