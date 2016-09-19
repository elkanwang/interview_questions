class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        num = num.split('0')
        for i, n in enumerate(num):
            if len(n) <= k and n:
                k -= len(n)
                del num[i]
        num = '0'.join(num)
        if not num:
            return '0'
        # print k, num
        index = 0
        while index < len(num) - 1 :
            if num[index] > num[index+1]:
                break
            index += 1
        while k:
            # print k, num
            if index == len(num)-1:
                num = num[:-1]
                index -= 1
            else:
                num = num[:index]+num[index+1:]
                while index < len(num) - 1:
                    if num[index] > num[index+1]:
                        break
                    index += 1
            k -= 1
        # print k, num
        return num.lstrip('0') if num != "0" else "0"

sol = Solution()
print sol.removeKdigits("1432219", 3)
print sol.removeKdigits("10200", 1)
print sol.removeKdigits("10", 1)
print sol.removeKdigits("1111111", 3)
print sol.removeKdigits("0", 0)


def removeKdigits(num, k):
    out = []
    for d in num:
        while k and out and out[-1] > d:
            out.pop()
            k -= 1
        out.append(d)
    return ''.join(out[:-k or None]).lstrip('0') or '0'

removeKdigits('1111111', 3)
removeKdigits("120800900", 2)
removeKdigits("1432219", 3)