"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

O(n)
"""

from dataclasses import dataclass
from typing import Type, List


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def min_depth(root: TreeNode) -> int:
    if root is None:
        return 0
    if root.left and root.right:
        return min(min_depth(root.left), min_depth(root.right)) + 1
    else:
        return max(min_depth(root.left), min_depth(root.right)) + 1


if __name__ == '__main__':
    print(min_depth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
