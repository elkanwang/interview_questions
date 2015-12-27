'''
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''

import heapq

class MedianFinder:
    small = []
    big = []
    def __init__(self):
        """
        Initialize your data structure here.
        """
        for i in self.small:
            self.small.pop()
        for j in self.big:
            self.big.pop()

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if -num > self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)
        if len(self.small) - len(self.big) == 2:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.big) - len(self.small) == 2:
            heapq.heappush(self.small, heapq.heappop(self.big))
        print self.small, self.big

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.big):
            return (self.big[0] - self.small[0])/2.0
        return -float(self.small[0]) if len(self.small) > len(self.big) else float(self.big[0])




# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
mf.addNum(3)
print mf.findMedian()
