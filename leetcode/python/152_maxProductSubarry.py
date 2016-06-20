class Solution:
	def maxProduct(self, nums):
		n = len(nums)
		if n < 1:
			return 0
		front_max = front_min = max_product = nums[0]
		for i in range(1, n):
			front_max, front_min = max(nums[i], nums[i]*front_max, nums[i]*front_min), \
								   min(nums[i], nums[i]*front_max, nums[i]*front_min)
			max_product = max(max_product, front_min, front_max)
		return max_product

sol = Solution()
print sol.maxProduct([-1, 1])