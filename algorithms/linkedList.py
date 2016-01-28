class linkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        tmp = self
        res = []
        while tmp:
            res.append(tmp.data)
        return res
