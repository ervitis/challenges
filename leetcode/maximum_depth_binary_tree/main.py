"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def max_depth(root: TreeNode) -> int:
    i = 0

    def search_depth(node: TreeNode, c: int) -> int:
        if node is None:
            return c
        a = search_depth(node.left, c+1)
        b = search_depth(node.right, c+1)
        return max(a, b)

    if root is None:
        return i
    return search_depth(root, i)


if __name__ == '__main__':
    print(max_depth(TreeNode(2, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
