class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_arr = [[] for i in range(n+1)]
        odd_nums = ['0', '1', '8']
        even_nums = ['00', '11', '88', '69', '96']
        if n == 0:
            return []
        elif n == 1:
            return odd_nums
        elif n == 2:
            return ['11', '88', '69', '96']
        res_arr[1] = ['0', '1', '8']
        res_arr[2] = ['11', '88', '69', '96']

        for i in range(3, (n+1)):
            if i % 2 == 1:
                # odd number
                prev_arr = res_arr[i-1]
                tmp_arr = []
                for number in prev_arr:
                    for n in odd_nums:
                        tmp_arr.append(number[:i/2] + n + number[i/2:])
                res_arr[i] = tmp_arr
            elif i % 2 == 0:
                # even number
                prev_arr = res_arr[i-2]
                tmp_arr = []
                for number in prev_arr:
                    for n in even_nums:
                        tmp_arr.append(number[:i/2-1] + n + number[i/2-1:])
                res_arr[i] = tmp_arr
        # print res_arr
        return res_arr[-1]

sol = Solution()
# print sol.findStrobogrammatic(1)
# print sol.findStrobogrammatic(2)
# print sol.findStrobogrammatic(3)
# print sol.findStrobogrammatic(4)
print sol.findStrobogrammatic(6)
