# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        hash_map = {}
        hash_map2 = {}
        counter = 0
        tmp = head
        new_head = None
        cur = None
        while tmp:
            if new_head is None:
                new_head = RandomListNode(tmp.label)
                cur = new_head
            else:
                new_node = RandomListNode(tmp.label)
                cur.next = new_node
                cur = new_node
            hash_map[tmp] = counter
            hash_map2[counter] = cur
            counter += 1
            tmp = tmp.next

        tmp = head
        new = new_head
        while tmp:
            print tmp.label, new.label
            if tmp.random is not None:
                random_next = tmp.random
                index = hash_map[random_next]
                new.random = hash_map2[index]
            tmp = tmp.next
            new = new.next
        return new_head


a = RandomListNode(1)
b = RandomListNode(2)
a.next = b
b.random = a

sol = Solution()
sol.copyRandomList(a)