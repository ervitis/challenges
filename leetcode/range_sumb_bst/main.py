"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
"""


from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


class Solution:
    def __init__(self):
        self.s = 0
        self.low = 0
        self.high = 0

    def range_sum_bst(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        self.low = low
        self.high = high

        self.do_sum(root)
        return self.s

    def do_sum(self, t: TreeNode) -> int:
        if not t:
            return 0
        if t.val > self.high:
            self.do_sum(t.left)
        if t.val < self.low:
            self.do_sum(t.right)

        if self.low <= t.val <= self.high:
            self.s += t.val
            self.do_sum(t.right)
            self.do_sum(t.left)


if __name__ == '__main__':
    tree = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18)))
    print(Solution().range_sum_bst(tree, 7, 15))
