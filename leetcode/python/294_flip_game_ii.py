# class Solution(object):
#     def canWin(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         me_arr = [[None]*len(s) for i in range(len(s))]
#         opponent_arr = [[None]*len(s) for i in range(len(s))]
#
#         def helper(s, start, end, isMe):
#             print 'calling helper on: ', start, end, isMe
#             if start == end:
#                 me_arr[start][end] = False if isMe else True
#                 # opponent_arr[start][end] = !me_arr[start][end]
#             elif end - start == 1:
#                 if s[start:end+1] == '++':
#                     me_arr[start][end] = True if isMe else False
#                 else:
#                     me_arr[start][end] = False if isMe else True
#             else:
#                 for start_index in range(start, end):
#                     print start, end, start_index
#                     if s[start_index: start_index+2] == '++':
#                         if start_index == start and start_index + 1 == end:
#                             # length == 2
#                             me_arr[start][end] = True if isMe else False
#                             # opponent_arr[start][end] = !me_arr[start][end]
#                         elif start_index == start:
#                             print 'start from left'
#                             # only look at right
#                             if me_arr[start_index+2][end] is None:
#                                 helper(s, start_index+2, end, not isMe)
#                             canWin = me_arr[start_index+2][end] if isMe else (not me_arr[start_index+2][end])
#                             print "can win? : ", canWin
#                             if canWin and isMe:
#                                 me_arr[start][end] = True
#                                 return
#                             if (not canWin) and (not isMe):
#                                 me_arr[start][end] = False
#                                 return
#                         elif start_index +1 == end:
#                             print 'start from right'
#                             # only look at left
#                             if me_arr[start][start_index-1] is None:
#                                 helper(s, start, start_index-1, not isMe)
#                             canWin = me_arr[start][start_index-1] if isMe else (not me_arr[start][start_index-1])
#                             print "can win? : ", canWin
#                             if canWin and isMe:
#                                 me_arr[start][end] = True
#                                 return
#                             if (not canWin) and (not isMe):
#                                 me_arr[start][end] = False
#                                 return
#                         else:
#                             # look at left and right
#                             if me_arr[start_index+2][end] is None:
#                                 helper(s, start_index+2, end, not isMe)
#                             if me_arr[start][start_index-1] is None:
#                                 helper(s, start, start_index-1, not isMe)
#                             canWin = me_arr[start_index+2][end] and me_arr[start][start_index-1]
#                             # print me_arr[start_index+2][end], me_arr[start][start_index-1]
#                             # canWin = not prevCanWin
#                             print "can win? : ", canWin
#                             if canWin and isMe:
#                                 me_arr[start][end] = True
#                                 return
#                             if (not canWin) and (not isMe):
#                                 me_arr[start][end] = False
#                                 return
#                 me_arr[start][end] = False if isMe else True
#         if not s:
#             return False
#         helper(s, 0, len(s)-1, True)
#         print me_arr
#         print '=============== answer ==============='
#         print me_arr[0][len(s)-1]
#         return me_arr[0][len(s)-1]
#
#
#
#
# sol = Solution()
# # sol.canWin('')
# # sol.canWin('-')
# sol.canWin('---')
# sol.canWin('++++')
# sol.canWin('+++')
# sol.canWin('+++++')


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s):
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    s = s[:i] + '--' + s[i+2:]
                    canWin = not helper(s)
                    if canWin:
                        return True
                    if not canWin:
                        s = s[:i] + '++' + s[i+2:]
            return False
        return helper(s)

sol = Solution()
print sol.canWin('')
print sol.canWin('-')
print sol.canWin('---')
print sol.canWin('++++')
print sol.canWin('+++')
print sol.canWin('+++++')
