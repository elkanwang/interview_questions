# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printIt(self):
        while self:
            print self.val
            self = self.next

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            front = l1
            head1 = l1.next
            head2 = l2
            while head1 and head2:
                if head2.val <= head1.val:
                    front.next = head2
                    head2 = head2.next
                    front = front.next
                    front.next = head1
                else:
                    front = front.next
                    head1 = head1.next
            if not head2:
                print 'a'
                pass
            else:
                print 'h'
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = head2
        else:
            # l2 is smaller
            head = l2
            front = l2
            head1 = l1
            head2 = l2.next
            while head1 and head2:
                if head1.val <= head2.val:
                    front.next = head1
                    head1 = head1.next
                    front = front.next
                    front.next = head2
                else:
                    front = front.next
                    head2 = head2.next
            if not head1:
                pass
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = head1
        return head


lst1 = ListNode(-10)
lst1.next = ListNode(-10)
lst1.next.next = ListNode(-9)
lst1.next.next.next = ListNode(-4)
lst2 = ListNode(-7)

sol = Solution()
list3 = sol.mergeTwoLists(lst2, lst1)
list3.printIt()