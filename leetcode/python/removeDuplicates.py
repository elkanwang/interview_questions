class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
        	return n
        index = 1
        nums1 = nums[0]
        nums2 = nums[index]
        count = 1
        while index < n:
        	if nums[index] == nums1:
        		nums.pop(index)
        		n -= 1
        	else:
        		nums1 = nums[index]
        		count += 1
        		index += 1
        return count


sol = Solution()
print sol.removeDuplicates([1,1,2,2,2,3])
print sol.removeDuplicates([])