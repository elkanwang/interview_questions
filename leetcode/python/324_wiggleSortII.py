class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        l, r = (1 + len(nums)) >> 1, len(nums)
        for i in xrange(len(nums)):
            if i & 1 == 1:
                r -= 1
                nums[i] = temp[r]
            else:
                l -= 1
                nums[i] = temp[l]






