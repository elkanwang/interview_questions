# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        while head and  head.val == val:
            head = head.next
        if head is None:
            return head
        tempHead = head.next
        lastHead = head
        while tempHead:
            if tempHead.val == val:
                lastHead.next = tempHead.next
                tempHead = lastHead.next
            else:
                lastHead = lastHead.next
                tempHead = tempHead.next
        return head
            