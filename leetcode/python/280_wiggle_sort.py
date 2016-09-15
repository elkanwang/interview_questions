class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_buf = sorted(nums)
        index = 0
        left = 0
        right = len(nums)-1
        while left <= right and index < len(nums):
            # print left, right, nums
            nums[index] = nums_buf[left]
            left += 1
            if left <= right:
                nums[index+1] = nums_buf[right]
                right -= 1
            index += 2
        print nums

    def wiggleSort2(self, nums):
        def swap(nums, i):
            tmp = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = tmp
        i = 0
        while i < len(nums):
            if i % 2 == 1:
                if nums[i] < nums[i-1]:
                    swap(nums, i)
            elif i !=0 and nums[i] > nums[i-1]:
                swap(nums, i)
            i += 1
        print nums

sol = Solution()
sol.wiggleSort2([3, 5, 2, 1, 6, 4, 7])
sol.wiggleSort2([1,2,3])
sol.wiggleSort2([2,1])