class MinStack:
    lst = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin is None:
            curMin = x
        elif x < curMin:
            curMin = x
        self.lst.append([x, curMin])
        

    # @return nothing
    def pop(self):
        self.lst.pop()

    # @return an integer
    def top(self):
        return self.lst[len(self.lst)-1][0]

    # @return an integer
    def getMin(self):
        if len(self.lst) == 0:
            return None
        else:
            return self.lst[len(self.lst)-1][1]
sol = MinStack()
sol.push(-2)
sol.push(0)
sol.push(-1)
print sol.getMin()
print sol.top()
sol.pop()
print sol.getMin()