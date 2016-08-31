class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        is_negative = (numerator * denominator) < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator / denominator
        res = str(integer_part) + '.'
        decimal = ""
        remainder = (numerator % denominator) * 10
        remainder_dict = {}
        index = 0
        while remainder and remainder not in remainder_dict:
            # print remainder
            remainder_dict[remainder] = index
            index += 1
            decimal += str(remainder / denominator)
            remainder = (remainder % denominator) * 10

        if not decimal:
            res = res[:-1]
        elif remainder in remainder_dict:
            res += decimal[:remainder_dict[remainder]] + '(' + decimal[remainder_dict[remainder]:] + ')'
        else:
            res += decimal
        return '-' + res if is_negative else res

sol = Solution()
print sol.fractionToDecimal(2, 3)
print sol.fractionToDecimal(1, 3)
print sol.fractionToDecimal(1, 8)
print sol.fractionToDecimal(8, 7)
print sol.fractionToDecimal(1, 6)
print sol.fractionToDecimal(-50, 8)
print sol.fractionToDecimal(0, 8)