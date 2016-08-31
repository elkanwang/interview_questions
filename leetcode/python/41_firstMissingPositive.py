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

    def firstMissingPositiveImproved(self, A):
        if A == []:
            return 1
        length = len(A)
        # pass 1
        for i in range(length):
            item = A[i]
            while item<=length and item>0 and A[item - 1] != item:
                temp = A[item-1]
                A[item-1] = A[i]
                A[i] = temp
                item = A[i]
        for i in range(length):
            if A[i] != i+1:
                return i+1
        return length+1


sol = Solution()
A = [3,4,-1,1]
print sol.firstMissingPositiveImproved(A)