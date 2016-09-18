import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        def gen(prime):
            print 'called gen with uglies {0} and prime {1}'.format(uglies, prime)
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            print ugly
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]

sol = Solution()
print sol.nthSuperUglyNumber(12, [2,7, 13, 19])