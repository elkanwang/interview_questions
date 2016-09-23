class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        post_text = ['', ' Thousand', ' Million', ' Billion']

        post_index = 0
        num = str(num)
        res = []

        def helper(char):
            char = int(char)
            if char == 0:
                return ''
            return ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'][char] + ' Hundred'

        def helper2(num):
            dict = {
                '0': 'Zero',
                '1': 'One',
                '2': 'Two',
                '3': 'Three',
                '4': 'Four',
                '5': 'Five',
                '6': 'Six',
                '7': 'Seven',
                '8': 'Eight',
                '9': 'Nine',
                '10': 'Ten',
                '11': 'Eleven',
                '12': 'Twelve',
                '13': 'Thirteen',
                '14': 'Fourteen',
                '15': 'Fifteen',
                '16': 'Sixteen',
                '17': 'Seventeen',
                '18': 'Eighteen',
                '19': 'Nineteen',
                '20': 'Twenty',
                '30': 'Thirty',
                '40': 'Forty',
                '50': 'Fifty',
                '60': 'Sixty',
                '70': 'Seventy',
                '80': 'Eighty',
                '90': 'Ninety'
            }
            if num in dict:
                return dict[num]
            else:
                if len(num) == 2:
                    return (['','','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'][int(num[0])] + ' ' +\
                           ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'][int(num[1])]).strip(' ')
                else:
                    return ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'][int(num[0])]

        while num:
            if len(num) >= 3:
                target = num[len(num)-3:]
            else:
                target = num
            tmp = ''
            if len(target) > 2:
                tmp = helper(target[0])
            if helper2(target[-2:]).strip(' '):
                if tmp:
                    tmp += ' '
                tmp += helper2(target[-2:]).strip(' ')

            if tmp:
                tmp += post_text[post_index]
                res.append(tmp)

            post_index += 1
            if len(num) <= 3:
                break
            num = num[:len(num)-3]

        # print res
        # print ' '.join(res[::-1])
        return ' '.join(res[::-1])

sol = Solution()
sol.numberToWords(1000)
sol.numberToWords(1234567891)
print sol.numberToWords(101) == "One Hundred One"
print sol.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"