# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow_ptr = head
        fast_ptr = head.next
        while fast_ptr:
            if fast_ptr != slow_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
                if not fast_ptr:
                    return False
                fast_ptr = fast_ptr.next
            else:
                return True
        return False