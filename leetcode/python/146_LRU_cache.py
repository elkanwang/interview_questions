class Node(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'node: ' +  str(self.key) + str(self.value)


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = None
        node.prev = None

    def insert(self, new_node):
        new_node.prev = self.tail
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def append(self, node_value):
        new_node = Node(node_value)
        self.insert(new_node)

    def __repr__(self):
        cur_node = self.head
        ll_str = ''
        while cur_node:
            ll_str += '{0} -> '.format(cur_node.value)
            cur_node = cur_node.next
        return ll_str + 'None'


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.ll = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.ll.remove(node)
            self.ll.insert(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.ll.remove(node)
            self.ll.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            if len(self.cache) <= self.capacity:
                self.ll.insert(node)
            else:
                # print key, value, self.cache, self.ll
                self.cache.pop(self.ll.head.key)
                self.ll.remove(self.ll.head)
                self.ll.insert(node)


# cache = LRUCache(1)
# # print cache.get(3)
# cache.set(2, 1)
# print cache.get(2)
# cache.set(3, 2)
# # cache.set(1992, 1992)
# print cache.get(2)
# # print cache.ll
# # cache.set(1993, 1993)
# # print cache.ll, cache.cache
# print cache.get(3)


cache = LRUCache(2)
cache.set(2, 1)
cache.set(1, 1)
print cache.ll
print cache.get(2)
print cache.ll
cache.set(4, 1)
print cache.get(1)
print cache.get(2)