# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printIt(self):
        res = []
        while self:
            res.append(self.val)
            self = self.next
        print res

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        tempHead = head
        print head.val
        if tempHead is None:
            return head
        while tempHead.next:
            if tempHead.val==tempHead.next.val:
                tempHead.next = tempHead.next.next
            tempHead = tempHead.next
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
sol = Solution()
sol.deleteDuplicates(node1).printIt()