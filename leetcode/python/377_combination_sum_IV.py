# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target == 0:
#             return 1
#         if target <0:
#             return 0
#         res = 0
#         for num in nums:
#             res += self.combinationSum4(nums, target-num)
#         return res



# use dp!!
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = [0] * (target+1)
        res[0] = 1
        for i in xrange(1, target+1):
            for j in nums:
                if i >= j:
                    res[i] += res[i-j]
        print res
        return res[target]


s = Solution()
print s.combinationSum4([4, 2, 1], 10)
