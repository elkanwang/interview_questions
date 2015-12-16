#!/usr/bin/env python
import unittest


class Node:
    '''
    data structure for linkedlist
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        temp = self
        while temp:
            print temp.data
            temp = temp.next


class Solution():
    '''
    Solution for chapter two:  linked list
    '''
    pass


class Test(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
