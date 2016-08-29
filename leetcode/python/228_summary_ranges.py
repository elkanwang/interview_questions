class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) <= 1:
            return map(lambda x: str(x), nums)

        res = []
        start = nums[0]
        end = start + 1
        for value in nums[1:]:
            if value == end:
                end += 1
            else:
                if end == start + 1:
                    res.append(str(start))
                else:
                    res.append("{0}->{1}".format(start, end-1))
                start = value
                end = value + 1

        if end == start + 1:
            res.append(str(start))
        else:
            res.append("{0}->{1}".format(start, end - 1))
        return res



sol = Solution()
print sol.summaryRanges([1])
print sol.summaryRanges([0,1,2,4,5,7,8])
print sol.summaryRanges([0,1])