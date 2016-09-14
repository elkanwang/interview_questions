# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        cur = self
        res = ''
        while cur:
            res += str(cur.val) + '-> '
            cur = cur.next
        return res

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        list_len = len(lists)
        if list_len == 0:
            return None
        elif list_len == 1:
            return lists[0]
        elif list_len == 2:
            return self.merge(lists[0], lists[1])
        else:
            l1 = self.mergeKLists(lists[:list_len/2])
            l2 = self.mergeKLists(lists[list_len/2:])
            # print l1, l2
            return self.merge(l1, l2)

    def merge(self, l1, l2):
        head = None
        cur = None
        while l1 and l2:
            if l1.val > l2.val:
                if head is None:
                    head = l2
                    cur = head
                else:
                    cur.next = l2
                    cur = l2
                l2 = l2.next
            else:
                if head is None:
                    head = l1
                    cur = head
                else:
                    cur.next = l1
                    cur = l1
                l1 = l1.next
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2
        # print 'merged', head
        return head

sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
print sol.mergeKLists([None, l3])