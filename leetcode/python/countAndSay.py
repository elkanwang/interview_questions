class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        sequence = "1"
        if n==0:
            return sequence
        i = 1
        while i<n:
            newSequence = ""
            length = len(sequence)
            count = 1
            index = 0
            curInt = sequence[index]
            index += 1
            while index < length:
                if sequence[index] == curInt:
                    count += 1
                else:
                    newSequence = newSequence + str(count) + curInt
                    curInt = sequence[index]
                    count = 1
                index += 1
            newSequence = newSequence + str(count) + curInt
            sequence = newSequence
            i+=1
        return sequence


sol = Solution()
print sol.countAndSay(5)
