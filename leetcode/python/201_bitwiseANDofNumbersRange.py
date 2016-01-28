import math

class Solution:
	def rangeBitwiseAnd(self, m, n):
		if m == n:
			return m
		diff = n ^ m
		index = int(math.floor(math.log(diff, 2))) + 1
		return m >> index << index


   	


sol = Solution()
print sol.rangeBitwiseAnd(1, 2)