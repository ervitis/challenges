"""
Given a binary tree, determine if it is height-balanced.
"""

from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def is_balanced(root: TreeNode) -> bool:
    def search(t: TreeNode) -> int:
        if t is None:
            return 0
        else:
            return max(search(t.left), search((t.right))) + 1

    if root is None:
        return True
    else:
        if abs(search(root.left) - search(root.right)) > 1:
            return False
        else:
            return is_balanced(root.left) and is_balanced(root.right)


if __name__ == '__main__':
    print(is_balanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(is_balanced(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))))
