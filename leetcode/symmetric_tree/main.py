"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""


from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def is_symmetric(root: TreeNode) -> bool:
    def is_mirror(left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outter = is_mirror(left.left, right.right)
            inner = is_mirror(left.right, right.left)
            return outter and inner
        else:
            return False

    if root is None:
        return True
    else:
        return is_mirror(root.left, root.right)


if __name__ == '__main__':
    print(is_symmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))
    print(is_symmetric(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))))
