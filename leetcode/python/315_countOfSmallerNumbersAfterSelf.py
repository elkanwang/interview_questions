'''
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].

'''


class Node(object):

    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.count = 0
        self.dup = 1

    def insert(self, insert_val, res_sofar):
        print('passing..... ', self.value, self.count, self.dup)
        if insert_val == self.value:
            self.dup += 1
            print('dup:', insert_val, self.count, self.dup)
            return self.count + res_sofar
        elif insert_val > self.value:
            if not self.right:
                self.right = Node(insert_val)
                # self.right.count = self.count + self.dup
                print('right:', insert_val, self.right.count, self.right.dup, res_sofar)
                return self.count + self.dup + res_sofar
            else:
                return self.right.insert(insert_val, res_sofar+ self.count + self.dup)
        elif insert_val < self.value:
            self.count += 1
            if not self.left:
                self.left = Node(insert_val)
                print('left:', insert_val, self.left.count, self.left.dup)
                return res_sofar
            else:
                return self.left.insert(insert_val, res_sofar)

class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, index, arr, val):
        if not self.root:
            self.root = Node(val)
            arr[index] = 0
        else:
            res = self.root.insert(val, 0)
            arr[index] = res




class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bst = BST()
        arr = [0] * len(nums)
        for i in reversed(range(len(nums))):
            bst.insert(i, arr, nums[i])
        print(arr)

sol = Solution()
# sol.countSmaller([2, 1, 1, 0])
print('\n')
# sol.countSmaller([5, 2, 6, 1])

sol.countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])