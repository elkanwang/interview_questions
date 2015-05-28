class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        i = 0
        while i<n:
            j=1
            gasLeft=0
            while j<=n:
                k = (i+j-1)%n
                gasLeft += gas[k]-cost[k]
                if gasLeft <0:
                	break
                j+=1
            if j>n:
                return i
            i+=j
        return -1

sol = Solution()
print sol.canCompleteCircuit([4],[5])
print sol.canCompleteCircuit([2,0,3],[1,2,2])