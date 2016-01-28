from collections import deque

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)

    # @return nothing
    def pop(self):
        q2 = deque()
        length = len(self.q)
        for i in xrange(length-1):
            q2.append(self.q.popleft())
        self.q = q2

    # @return an integer
    def top(self):
        q2 = deque()
        length = len(self.q)
        for i in xrange(length-1):
            q2.append(self.q.popleft())
        res = self.q.popleft()
        q2.append(res)
        self.q = q2
        return res

    # @return an boolean
    def empty(self):
        return len(self.q) == 0

print Stack().push(1)