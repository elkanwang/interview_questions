class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        data = map(lambda a:"{0:08b}".format(a), data)
        index = 0
        while index < len(data):
            expected_continuition = len(data[index].split('0')[0])
            # print expected_continuition
            if expected_continuition == 0:
                index += 1
            elif expected_continuition == 2:
                if index+1 >= len(data):
                    return False
                if data[index+1][:2] == '10':
                    index += 2
                else:
                    return False
            elif expected_continuition == 3:
                if index+2 >= len(data):
                    return False
                if data[index+1][:2] == '10' and data[index+2][:2] == '10':
                    index += 3
                else:
                    return False
            elif expected_continuition == 4:
                if index+2 >= len(data):
                    return False
                if data[index+1][:2] == '10' and data[index+2][:2] == '10' and data[index+3][:2] == '10':
                    index += 4
                else:
                    return False
            else:
                return False
        return True




sol = Solution()
print sol.validUtf8( [197, 130, 1])
print sol.validUtf8( [235, 140, 4])
print sol.validUtf8( [255])
print sol.validUtf8([240,162,138,147])