 class BinaryIndexedTree(object):
    """

    """
    tree = None

    def __init__(self, nums):
        self.tree = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            lowbit = i & -i
            cum = 0
            for j in range(lowbit):
                cum += nums[i-j-1]
            self.tree[i] = cum

    def update(self, index, inc):
        index += 1
        while index < len(self.tree):
            self.tree[index] += inc
            index += index & (-index)

    def sum_range(self, start, end):
        return self.get_sum(end) - self.get_sum(start-1)

    def get_sum(self, index):
        res = 0
        index += 1
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res




bit = BinaryIndexedTree([1,2,3,4,5,6,7,8,9])
print bit.tree
print bit.get_sum(8)
print bit.sum_range(4,8)