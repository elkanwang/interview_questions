class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        res = sorted(A+B)
        if len(res) == 0:
            return 0
        elif len(res) % 2 == 0:
            return float(res[len(res)/2]+ res[len(res)/2 - 1])/2
        else:
            return res[len(res)/2]

    def findMedianSortedArraysImproved(self, A, B):
    	length = len(A) + len(B)
    	if length % 2 == 0:
    		return float(self.kth(A,B,length/2) + self.kth(A,B,length/2-1))/2
    	else:
    		return self.kth(A,B,length/2)

    def kth(self, A, B, k):
    	if not A:
    		return B[k]
    	if not B:
    		return A[k]

    	ia, ib = len(A)/2, len(B)/2
    	ma, mb = A[ia], B[ib]

    	if ia + ib >= k:
    		if ma > mb:
    			return self.kth(A[:ia],B,k)
    		else:
    			return self.kth(A,B[:ib],k)
    	else:
    		if ma > mb:
    			return self.kth(A,B[ib+1:],k-ib-1)
    		else:
    			return self.kth(A[ia+1:],B,k-ia-1)

sol = Solution()
A = []
B = [2,3]
print sol.findMedianSortedArrays(A,B)
