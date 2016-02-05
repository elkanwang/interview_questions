class Solution(object):

    '''
    1. sorted -> find the one that doesn't equal to the index
    2. use xor
    '''

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)+1
        res = 0
        for i in range(1,n):
            res ^= i
        for num in nums:
            res ^= num
        return res

sol = Solution()
print sol.missingNumber([0,1,3])
