'''
Convert a non-negative integer to its english words representation. Given input
is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''


class Solution(object):

   numDict = {
    '0': "",
    '1': "One",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
   }

   tensDict = {
    '10': "Ten",
    '11': "Eleven",
    '12': "Twlve",
    '13': "Thirteen",
    '14': "Fourteen",
    '15': "Fifteen",
    '16': "Sixteen",
    '17': "Seventeen",
    '18': "Eighteen",
    '19': "Ninteen",
    '2': "Twenty",
    '3': "Thirty",
    '4': "Forty",
    '5': "Fifty",
    '6': "Sixty",
    '7': "Seventy",
    '8': "Eighty",
    '9': "Ninty"
   }


   def helper(self, num):
        """
        :type num: str
        :rtype: str
        """
        num = str(int(num))
        num = list(num)
        if len(num) == 1:
            return self.numDict.get(num[0])
        elif len(num) == 2

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
