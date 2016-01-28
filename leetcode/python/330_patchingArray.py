# coding=UTF-8

'''
Given a sorted positive integer array nums and an integer n, add/patch elements
to the array such that any number in range [1, n] inclusive can be formed by the
sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
'''

class Solution(object):
    '''
    greedy
    
    1. 把所有的combination都放在set里
    2. 从最小开始loop，找到后，加进set里
    3. 一直loop到n

    方法一把memory给高爆炸了。。

    方法二：
    就是用known_sum表示已知的连续和为[1,known_sum)，有了这个表示那就简单了：
        nums[i] <= known_sum，更新已知范围为：[1,known_sum + nums[i] )
        nums[i] >  known_sum,  添加known_sum进数组才能达到最大的范围，所以已知范围更新为：[1,known_sum *2)
    '''
    def minPatches(self, nums, n):
        i, miss, added = 0, 1, 0
        numsLen = len(nums)
        while miss <= n:
            if (i<numsLen and nums[i]<=miss):
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added




    def minPatches1(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        pool = set()
        def permutations(nums):
            if len(nums) == 0:
                return
            pool.add(sum(nums))
            for i in xrange(len(nums)):
                permutations(nums[:i]+nums[i+1:])
        permutations(nums)
        res = 0
        for i in range(1,n+1):
            if i not in pool:
                res += 1
                temp = [i]
                for m in pool:
                    temp.append(i+m)
                for m in temp:
                    pool.add(m)
        return res

s = Solution()
# print s.minPatches([1,2,2],5)
print s.minPatches([1,2,31,33],2147483647)
print s.minPatches([1,5,10], 20)
