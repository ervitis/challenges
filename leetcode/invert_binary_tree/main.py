"""
Invert a binary tree
"""

from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return root

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)
    return root


if __name__ == '__main__':
    print(invert_tree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))
