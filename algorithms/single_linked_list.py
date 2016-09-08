class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList(object):
    head = None
    tail = None

    def __init__(self):
        pass

    def show(self):
        current_node = self.head
        node_str = ''
        while current_node:
            node_str += '{0} -> '.format(current_node.data)
            current_node = current_node.next
        print node_str + 'None'

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        if self.head is None:
            return
        prev, cur = self.head, self.head.next
        if prev.data == node_value:
            self.head = self.head.next
        while cur:
            if cur.data == node_value:
                prev.next = cur.next
                return
            else:
                pre, cur = cur, cur.next


ll = SingleLinkedList()
ll.append(5)
ll.append(1)
ll.append(3)
ll.show()
ll.remove(1)
ll.show()
