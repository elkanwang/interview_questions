class Node(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'tail: ' + str(self.data)

class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def show(self):
        cur_node = self.head
        ll_str = ''
        while cur_node:
            ll_str += "{0} -> ".format(cur_node.data)
            cur_node = cur_node.next
        print ll_str + 'None'

    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        cur_node = self.head
        while cur_node:
            if cur_node.data == node_value:
                if cur_node.prev is not None:
                    cur_node.prev.next = cur_node.next
                else:
                    self.head = cur_node.next
                if cur_node.next is not None:
                    cur_node.next.prev = cur_node.prev
                else:
                    self.tail = cur_node.prev
            cur_node = cur_node.next

ll = DoublyLinkedList()
ll.append(5)
ll.append(3)
ll.append(2)
ll.append(1)
ll.show()
print ll.tail
ll.remove(3)
ll.show()
print ll.tail
ll.remove(1)
ll.show()
print ll.tail
ll.remove(5)
ll.show()