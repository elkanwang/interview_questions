class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        neighbours = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbours[pre].add(course)
        S = [n for n in range(numCourses) if not graph[n]]
        count = 0
        while S:
            node = S.pop()
            count += 1
            for n in neighbours[node]:
                graph[n].remove(node)
                if not graph[n]:
                    S.append(n)
        return count==numCourses