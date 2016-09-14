class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1_index = 0
        self.v2_index = 0
        self.v1 = v1
        self.v1_len = len(v1)
        self.v2 = v2
        self.v2_len = len(v2)

        self.ptr = 0

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return
        res = None
        if self.ptr == 0:
            if self.v1_index == self.v1_len:
                self.ptr = 1
                res = self.v2[self.v2_index]
                self.v2_index += 1
            else:
                res = self.v1[self.v1_index]
                self.v1_index += 1
                self.ptr = 1
        else:
            if self.v2_index == self.v2_len:
                self.ptr = 0
                res = self.v1[self.v1_index]
                self.v1_index += 1
            else:
                res = self.v2[self.v2_index]
                self.v2_index += 1
                self.ptr = 0
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.v1_index == self.v1_len and self.v2_index == self.v2_len:
            return False
        else:
            return True

v1 = [1, 2]
v2 = [3, 4, 5, 6]

z = ZigzagIterator(v1, v2)
while z.hasNext():
    print z.next()
