class Solution(object):
    table = {}

    def calculate(self, nums, i):
        if i == 0 and len(nums) == 1:
            return nums[0]
        if i == 0:
            return nums[0] * nums[1]
        if i == len(nums) - 1:
            return nums[i] * nums[i - 1]
        return nums[i - 1] * nums[i] * nums[i + 1]

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_tuple = tuple(nums)
        if nums_tuple in self.table:
            return self.table[nums_tuple]
        res = []
        for i, number in enumerate(nums):
            res.append(self.calculate(nums, i) + self.maxCoins(nums[:i] + nums[i + 1:]))
        self.table[tuple(nums)] = max(res)
        return self.table[nums_tuple]


sol = Solution()
print sol.maxCoins([3, 1, 5, 8])
print sol.maxCoins([8, 2, 6, 8, 9, 8, 1, 4, 1, 5, 3, 0, 7, 7, 0, 4, 2, 2])
