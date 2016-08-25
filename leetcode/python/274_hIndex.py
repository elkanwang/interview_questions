'''
Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.


For example, given citations = [3, 0, 6, 1, 5], which means the researcher has
5 papers in total and each of them had received 3, 0, 6, 1, 5 citations
respectively. Since the researcher has 3 papers with at least 3 citations each
and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as
the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.
'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations)
        for i in reversed(range(0, len(citations)+1)):
            print(i, citations[-i], citations[-i], citations)
            if citations[-i] >= i:
                if len(citations) - i == 0:
                    return i
                if citations[-i-1] <= i:
                    return i
        return 0
sol = Solution()

print(sol.hIndex([3, 0, 6, 1, 5]))
print(sol.hIndex([5, 5, 6, 6, 5]))
print(sol.hIndex([]))
print(sol.hIndex([1, 1]))