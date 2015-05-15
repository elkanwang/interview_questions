class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        length = len(nums)
        result = nums[:]
        k = k % length
        for i in range(length):
            result[i+k-length] = nums[i]
        for i in range(length):
        	nums[i] = result[i]

sol = Solution()
sol.rotate([1,2],1)