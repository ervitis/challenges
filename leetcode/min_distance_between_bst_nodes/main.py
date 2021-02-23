"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
"""


from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


class Solution(object):

    def __init__(self):
        self.last = None
        self.min_diff = None

    def min_diff_in_bst(self, root: TreeNode) -> int:
        self.last = float('-inf')
        self.min_diff = float('inf')

        self.in_order(root)

        return int(self.min_diff)

    def in_order(self, node: TreeNode):
        if not node:
            return
        self.in_order(node.left)
        self.min_diff = min(self.min_diff, node.val - self.last)
        self.last = node.val
        self.in_order(node.right)


if __name__ == '__main__':
    s = Solution()
    print(s.min_diff_in_bst(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))
