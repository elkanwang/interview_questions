# def solution(A, B):
#     # write your code in Python 2.7
#     binary = '{0:b}'.format(A*B)
#     print binary
#     return binary.count('1')
#
#
# print solution(3,7)
# print solution(2,4)


def solution(S):
    # write your code in Python 2.7
    leftmost = 0
    while leftmost < len(S):
        if S[leftmost] == '1':
            break
        else:
            leftmost += 1
    index = len(S) - 1
    count = 0
    while index > leftmost:
        if S[index] == '0':
            count += 1
        else:
            count += 2
        index -= 1
    if S[leftmost] == '1':
        count += 1
    return count
print solution('011100')
print solution('000010110101010')
print int('000010110101010', 2)
# def solution(S):
#     # write your code in Python 2.7
#     if not S:
#         return 0
#     left = 0
#     while left < len(S):
#         if S[left] == '(':
#             break
#         else:
#             left += 1
#     right = len(S) - 1
#     while right > left:
#         if S[right] == ')':
#             break
#         else:
#             right -= 1
#     while left < right:
#         left += 1
#         while left < right:
#             if S[left] == '(':
#                 break
#             else:
#                 left += 1
#         if left >= right:
#             return right
#         right -= 1
#         while right > left:
#             if S[right] == ')':
#                 break
#             else:
#                 right -= 1
#     return left
#
#
# print solution(')))))')
# print solution('(())')
# print solution('(())))()')
# print solution('()')
# print solution('(')
# print solution('')
# print solution('))(())((')