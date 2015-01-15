# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            n = 0
            sum = (l1.val+l2.val+n) % 10
            n = (l1.val+l2.val+n) /10
            ret = ListNode(sum)
            temp = ret
            while l1.next or l2.next:
                if l1.next is None:
                    l2 = l2.next
                    sum = (l2.val+n) % 10
                    n = (l2.val+n) / 10
                    temp.next = ListNode(sum)
                    temp = temp.next
                elif l2.next is None:
                    l1 = l1.next
                    sum = (l1.val+n) % 10
                    n = (l1.val+n) / 10
                    temp.next = ListNode(sum)
                    temp = temp.next
                else:
                    l1 = l1.next
                    l2 = l2.next
                    sum = (l1.val+l2.val+n) % 10
                    n = (l1.val+l2.val+n) /10
                    temp.next = ListNode(sum)
                    temp = temp.next
            if n == 1:
                temp.next = ListNode(1)
            return ret