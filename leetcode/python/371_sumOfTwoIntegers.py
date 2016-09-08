class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a = list('{0:b}'.format(a)[::-1])
        b = list('{0:b}'.format(b)[::-1])
        len_a = len(a)
        len_b = len(b)
        res = []
        offset = 0
        for index in range(max(len_a, len_b)):
            if index >= len_a:
                cur_a = 0
                cur_b = b[index]
            elif index >= len_b:
                cur_b = 0
                cur_a = a[index]
            else:
                cur_a = a[index]
                cur_b = b[index]

            if cur_a == '1' and cur_b == '1' and offset == 1:
                res.append('1')
                offset = 1
            else:
                cur = offset ^ int(cur_a) ^ int(cur_b)
                if cur_a == '1' or cur_b == '1' or offset == 1:
                    if cur == 0:
                        offset = 1
                    else:
                        offset = 0
                    res.append(str(cur))
                else:
                    offset = 0
                    res.append(str(cur))
        if offset == 1:
            res.append('1')
        return int(''.join(res)[::-1], 2)


sol = Solution()
print sol.getSum(5,8)
print sol.getSum(124,125)