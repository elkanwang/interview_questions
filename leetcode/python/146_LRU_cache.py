class Node(object):

    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.linked_list_head = Node()
        self.linked_list_tail = Node()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            pass
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
            node_left = node.left
            node_right = node.right
            node_left.right = node_right
            node_right.left = node_left
            res_value = node.value[1]
            # insert back
            node.value = (key, value)
            node.right = self.linked_list_head
            self.linked_list_tail.left = node
            return res_value
        elif len(self.cache) < self.capacity:
            node = Node()
            node.value = (key, value)
            node.right = self.linked_list_head
            self.linked_list_tail.left = node
            self.cache[key] = node
        else:
            # remove right most
            node_to_delete = self.linked_list_tail
            key_to_delete = node_to_delete.value[0]
            del self.cache[key_to_delete]
            self.linked_list_tail = node_to_delete.left
            node_to_delete.left.right = None


