class Solution:
    # @return an integer
    def reverse(self, x):
        if x < 0:
            s = str(0-x)
            s = s[::-1]
            x = 0-int(s)
        else:
            s = str(x)[::-1]
            x = int(s)
        if x > math.pow(2,31) or x < -math.pow(2,31):
            x = 0
        return x