class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        n = len(nums)
        nums = sorted(nums)
        subset_list = [[] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    subset = subset_list[j] + [nums[i]]
                    if len(subset) > len( subset_list[i]):
                        subset_list[i] = subset
            if subset_list[i] == []:
                subset_list[i] = [nums[i]]

        subset_list.sort(key=lambda s: len(s))
        return subset_list[-1]

sol = Solution()
print(sol.largestDivisibleSubset([1,2,3]))
print(sol.largestDivisibleSubset([3,4,16,8]))
print(sol.largestDivisibleSubset([1,2,4,7,8]))