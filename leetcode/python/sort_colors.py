class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        red = 0
        blue = len(nums) - 1
        index = 0
        while index <= blue and blue >=0 and red < len(nums):
            # print index, nums
            if nums[index] == 0:
                if index == red:
                    red += 1
                    index += 1
                    continue
                tmp = nums[red]
                nums[red] = 0
                nums[index] = tmp
                red += 1
                continue
            if nums[index] == 1:
                index += 1
                continue
            if nums[index] == 2:
                tmp = nums[blue]
                nums[blue] = 2
                nums[index] = tmp
                blue -= 1
                continue
        # print nums
        return

sol = Solution()
sol.sortColors([1,2,0,0,1,2])
sol.sortColors([0, 1])


