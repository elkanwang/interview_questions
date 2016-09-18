class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        def gen(total_len, num):
            if num == 0:
                return ['0'*total_len]
            if total_len == num:
                return ['1'*total_len]
            res = []
            for n in gen(total_len-1, num):
                res.append('0'+n)
            for n in gen(total_len-1, num-1):
                res.append('1'+n)
            return res
        # print gen(6, 0)
        # print gen(6, 2)
        def produce_hour(num):
            res = filter(lambda x: x < 12, map(lambda x: int(''.join(x), 2), gen(4, num)))
            return res

        def produce_minute(num):
            res = filter(lambda x: x <= 59, map(lambda x: int(''.join(x), 2), gen(6, num)))
            return res

        res = []
        for i in range(min(num+1, 5)):
            hours = produce_hour(i)
            minutes = produce_minute(num-i)
            for hour in hours:
                for minute in minutes:
                    res.append(str(hour) + ":" + '{0:02}'.format(minute))
        return res

sol = Solution()
print sol.readBinaryWatch(7)