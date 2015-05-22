# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        index = length - n 
        if index == 0:
            return head.next
        temp = head
        while index - 1 > 0:
            index -= 1
            temp = temp.next
        if temp.next is None:
            return head
        temp.next = temp.next.next
        return head

sol = Solution()
sol.removeNthFromEnd(ListNode(1), 0)