# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        prev = None
        while tmp:
            next = tmp.next
            if not next:
                return head
            tmp.next = next.next
            next.next = tmp
            if prev is not None:
                prev.next = next
            prev = tmp
            tmp = tmp.next
        return head