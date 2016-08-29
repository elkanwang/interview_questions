# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return  'start: ' + str(self.start) + ' end: ' + str(self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]

        proposed solution:
        arrange by end time
        """
        res = []

        def _find_end_index(res_arr, end):
            for index, interval in enumerate(res_arr):
                if interval.end >= end:
                    return index
            return len(res_arr) + 1

        def _find_start_index(res_arr, start):
            for index, interval in enumerate(res_arr):
                if interval.end >= start:
                    return index
            return len(res_arr) + 1

        for interval in intervals:
            end = interval.end
            start = interval.start
            start_index = _find_start_index(res, start)
            end_index = _find_end_index(res, end)
            if start_index > len(res) and end_index > len(res):
                res.append(interval)
            elif end_index > len(res):
                new_start = min(start, res[start_index].start)
                res = res[:start_index]
                res.append(Interval(new_start, end))
            elif end_index == 0:
                if res[0].start > end:
                    res = [interval] + res
                else:
                    res[0].start = min(res[0].start, start)
            else:
                if end < res[end_index].start:
                    new_start = min(start, res[start_index].start)
                    res = res[:start_index] + [Interval(new_start, end)] + res[end_index:]
                else:
                    new_start = min(start, res[start_index].start)
                    new_end = res[end_index].end
                    res = res[:start_index] + [Interval(new_start, new_end)] + res[end_index+1:]

            print res
            print start_index, end_index
        return res

sol = Solution()
# interval_arr = [Interval(1,3), Interval(-3, -1), Interval(8,10),  Interval(2,6), Interval(5,9), Interval(15, 18)]
interval_arr = [Interval(1,4), Interval(0,4)]

print sol.merge(interval_arr)
