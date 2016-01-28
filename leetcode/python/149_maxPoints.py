# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

p1 = Point(0,0)
p2 = Point(1,0)
class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if len(points) == 0: return 0
        res = 1
        for i,p in enumerate(points[:-1]):
            d = {}
            psame = 1
            for q in points[i+1:]:
                if p.x==q.x and p.y==q.y:
                    psame+=1
                    continue
                elif p.x==q.x:
                    key = "INF"
                else:
                    key = float(p.y-q.y)/(p.x-q.x)
                d[key] = d.get(key,0)+1
            try:
                temp = max(d.values())
            except:
                temp = 0
            res = max(res, temp+psame)
        return res

sol = Solution()
print sol.maxPoints([p1, p2])