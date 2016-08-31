class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        swap_index = None
        cur_max = nums[-1]

        for index in reversed(range(len(nums))):
            if nums[index] < cur_max:
                swap_index = index
                break
            else:
                cur_max = nums[index]

        if swap_index is None:
            length = len(nums)
            for index in range(length / 2):
                tmp = nums[index]
                nums[index] = nums[length - index - 1]
                nums[length - index - 1] = tmp
        else:
            for index in reversed(range(swap_index + 1, len(nums))):
                if nums[index] > nums[swap_index]:
                    tmp = nums[index]
                    nums[index] = nums[swap_index]
                    nums[swap_index] = tmp
                    break

            i, j = swap_index + 1, len(nums) - 1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        print nums


sol = Solution()
sol.nextPermutation([1, 2, 3, 4])
sol.nextPermutation([4, 3, 2, 1])
sol.nextPermutation([1, 5])
sol.nextPermutation([2, 3, 1])
