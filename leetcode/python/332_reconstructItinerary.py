class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = []
        def helper(start, tickets, path):

            if not tickets:
                res.append(path)
            ends = []
            for i, ticket in enumerate(tickets):
                if ticket[0] == start:
                    ends.append((ticket[1],i))
            if not ends:
                return
            for end in ends:
                p = list(path)
                p.append(end[0])
                b = tickets[:]
                del b[end[1]]
                helper(end[0], b, p)

        helper('JFK',list(tickets), ['JFK'])
        return sorted(res)[0]

sol = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print sol.findItinerary(tickets)
