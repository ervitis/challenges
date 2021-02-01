"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
"""

from dataclasses import dataclass
from typing import Type, List


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def level_order_bottom(root: TreeNode) -> List[List[int]]:
    lst = []

    if root is None:
        return lst
    nodes = [root]
    while nodes:
        lst.append([n.val for n in nodes])
        nn = []
        for n in nodes:
            if n.left:
                nn.append(n.left)
            if n.right:
                nn.append(n.right)
        nodes = nn
    return lst[::-1]


if __name__ == '__main__':
    print(level_order_bottom(TreeNode(3, TreeNode(9, TreeNode(20, TreeNode(15), TreeNode(7))))))
