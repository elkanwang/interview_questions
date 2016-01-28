class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        n = len(nums)
        if n < 2:
        	return 0
        curMax = nums[0]
        for i in range(n):
        	if nums[i] >= curMax:
        		curMax = nums[i]
        	else:
        		return i-1
        return n-1

sol = Solution()
print sol.findPeakElement([1,2, 3])