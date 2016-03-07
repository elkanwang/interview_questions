#coding=UTF-8
class Solution(object):
    '''
    这个问题很好回答，如果我们令l[k]表示f数组中值为k的一段的左边界，r[k]表示f数组中值为k的一段的有边界，那么有

    l[k] = r[k - 1] + 1，这是显然的
    r[k] = max{i + nums[i] | l[k - 1] <= i <= r[k - 1]}，由于f值为k的位置一定是从f值为k-1的位置走来的，所以只需要看从所有f值为k-1的位置里最远可以到达的地方即可。
    也就是说，我们可以在对nums的一遍扫描中，依次求出所有的l[k]和r[k]，而f数组也就自然求解出来了——答案也就得到了。

    这道题目虽然在LeetCode上标记为Hard，但是最后得出的解决方法也不算特别的复杂，主要是利用转换后最短路问题的一些特殊性质得到了非常有用的结论，来加速了整个最短路径的计算。
    http://www.tianmaying.com/tutorial/LC45
    '''
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k,l,r = 0,0,0
        if len(nums) == 1:
            return 0
        while r < len(nums) - 1:
            next_r = r
            for i in range(l, r+1):
                next_r = max(next_r,nums[i]+i)
            k+= 1
            l = r+1
            r = next_r
        return k

sol = Solution()
print sol.jump([2,3,1,1,4])
