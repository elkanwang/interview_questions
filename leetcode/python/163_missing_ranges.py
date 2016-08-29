class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]

        1. insert max value, and get rid of all the bigger values
        2. insert min value, and get rid of all the smaller values
        3. use the new num array to produce the array of ranges
        """

        max_inclusive = False
        min_inclusive = False

        def insert_max(nums, max):
            for i in reversed(range(len(nums))):
                if nums[i] < max:
                    return nums[:i+1] + [max], False
                elif nums[i] == max:
                    return nums[:i+1], True
            return [max], False

        def insert_min(nums, min):
            for i in range(len(nums)):
                if nums[i] > min:
                    return [min] + nums[i:], False
                elif nums[i] == min:
                    return nums[i:], True
            return [min], True

        def print_ranges(nums, min_inclusive, max_inclusive):
            if len(nums) == 1 and (not min_inclusive or not max_inclusive):
                return [str(nums[0])]
            if not min_inclusive:
                nums[0] -= 1
            if not max_inclusive:
                nums[-1] += 1
            res = []
            for i in range(len(nums)-1):
                small = nums[i]
                big = nums[i+1]
                if big - small < 2:
                    continue
                elif big - small == 2:
                    res.append(str(big-1))
                else:
                    res.append(str(small+1) + "->" + str(big-1))
            return res


        nums, max_inclusive = insert_max(nums, upper)
        nums, min_inclusive = insert_min(nums, lower)
        return print_ranges(nums, min_inclusive, max_inclusive)

sol = Solution()
print sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
print sol.findMissingRanges([], 1, 3)
print sol.findMissingRanges([], 1, 1)