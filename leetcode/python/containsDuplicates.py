class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        pool = {}
        for i in xrange(len(nums)):
            if nums[i] in pool.keys():
                pool[nums[i]] += 1
            else:
                pool[nums[i]] = 1
        length = filter(lambda x: x > 1, pool.values())
        return len(length) > 0

print Solution().containsDuplicate([1,2,3,3,5])