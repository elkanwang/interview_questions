import Queue

# class MovingAverage(object):
#     def __init__(self, size):
#         """
#         Initialize your data structure here.
#         :type size: int
#         """
#         self.window = []
#         self.size = size
#
#     def next(self, val):
#         """
#         :type val: int
#         :rtype: float
#         """
#         if len(self.window) == self.size:
#             self.window = self.window[1:] + [val]
#         else:
#             self.window.append(val)
#         return sum(self.window) / len(self.window)


import collections


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue)) / len(queue)

        # Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print obj.next(2)
print obj.next(1)
print obj.next(10)
print obj.next(1)