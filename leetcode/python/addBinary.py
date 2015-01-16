
def add(a,b,carryover,result):
    if len(a)>0 and len(b)>0:
        sum = int(a[0])+int(b[0])+carryover
        carryover = sum / 2
        result += str(sum % 2)
        a = a[1:]
        b = b[1:]
        return add(a,b,carryover,result)
    elif len(a)>0:
        if carryover==1:
            sum = int(a[0])+carryover
            carryover = sum / 2
            result +=  str(sum % 2)
            a = a[1:]
            return add(a,b,carryover,result)
        else:
            result += a
            return result
    elif len(b)>0:
        if carryover==1:
            sum = int(b[0])+carryover
            carryover = sum / 2
            result +=  str(sum % 2)
            b = b[1:]
            return add(a,b,carryover,result)
        else:
            result += b
            return result
    else:
        if carryover==1:
            result += '1'
        return result


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string

    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]
        sum = add(a,b,0,'')[::-1]
        return sum

