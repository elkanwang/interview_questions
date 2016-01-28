# class Solution:
#     # @param {integer[]} nums
#     # @return {integer}
#     def singleNumber(self, nums):
#         pool = {}
#         for n in nums:
#         	if pool.get(n):
#         		pool[n] += 1
#         	else:
#         		pool[n] = 1
#         for k, v in pool.iteritems():
#         	if v == 1:
#         		return k

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
    	if len(nums) == 0:
    		return 0
    	res = nums[0]
    	for i in range(1, len(nums)):
    		res = nums[i] ^ res
    	return res

sol = Solution()
print sol.singleNumber([1,1,2,2,3])