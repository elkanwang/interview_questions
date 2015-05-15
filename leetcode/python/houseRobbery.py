class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def robDP(self, nums, array):
        if len(nums) == 0:
        	return 0
        elif len(nums) == 1:
        	return nums[0]
        elif len(nums) == 2:
        	return max(nums[0],nums[1])
        else:
        	if array[-len(nums)] is not None:
        		return array[-len(nums)]
        	else :
        		array[-len(nums)] = max(nums[0] + self.robDP(nums[2:], array), nums[1] + self.robDP(nums[3:], array))
        		return array[-len(nums)]
    def rob(self, nums):
    	length = len(nums)
    	array = [None]*length
    	return self.robDP(nums,array)

sol = Solution()
# print [1,2,3][-3]
print sol.rob([6,6,4,8,4,3,3,10])
