class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
#    def myPow(self, x, n):
#        if n < 0:
#            n = -n
#            x = 1/x
#        res = 1
#        while n > 0:
#            res = res * x
#            n 
#        return res
#		
#	recursive
	def myPow(self, x, n):
		if n == 0:
			return 1
		elif n < 0 :
			return self.myPow(1/x, -n)
		if n % 2 :
			return x*self.myPow(x, n-1)
		else:
			return self.myPow(x*x, n/2)
#	iteration
	def myPow(self, x, n):
		if n == 0:
			return 1
		if n < 0:
			n = -n
			x = 1/x
		res = 1
		while n:
			if n & 1:
				res *= x
			x *= x
			n >>= 1
		return res
