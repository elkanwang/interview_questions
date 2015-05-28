import collections
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def findOrder(self, numCourses, prerequisites):
        L = []
        graph = collections.defaultdict(set)
        neighbours = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbours[pre].add(course)
        S = [n for n in range(numCourses) if not graph[n]]
        while S:
            node = S.pop()
            L.append(node)
            for n in neighbours[node]:
                graph[n].remove(node)
                if not graph[n]:
                    S.append(n)
        if len(L) != numCourses:
            return []
        else:
            return L

sol = Solution()
print sol.canFinish(4, [[1,0],[2,0],[3,1],[3,2]])