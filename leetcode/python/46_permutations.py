'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for num in nums:
            tmp = []
            for i in range(len(res)):
                for j in range(len(res[i])+1):
                    tmp.append(res[i][:j]+[num]+res[i][j:])
            if not tmp:
                tmp.append([num])
            print tmp
            res = tmp
        return res

sol = Solution()
print sol.permute([1,2,3])
