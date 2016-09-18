class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total_sum = sum(A)
        len_a = len(A)
        cur_max = 0
        for index, n in enumerate(A):
            cur_max += index * n
        res = [cur_max]
        for i in reversed(range(len_a)):
            cur_max = cur_max + total_sum - A[i] * len_a
            res.append(cur_max)
        return max(res)

sol = Solution()
print sol.maxRotateFunction([4,3,2,6])
