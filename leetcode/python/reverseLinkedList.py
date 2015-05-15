# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList1(self, head):
        newHead = None
        while head:
            tempHead = head
            head = head.next
            tempHead.next = newHead
            newHead = tempHead
        return newHead

    def reverseList2(self, head, last=None):
        if not head:
            return last
        next = head.next
        head.next = last
        return reverseList2(next, head)
