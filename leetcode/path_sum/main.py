# -*- coding: utf-8 -*-

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def path_sum(root: TreeNode, s: int) -> bool:
    if root is None:
        return s == 0
    else:
        s -= root.val
        t = False
        if s == 0:
            return True
        if root.right is not None:
            t = t or path_sum(root.right, s)
        if root.left is not None:
            t = t or path_sum(root.left, s)

        return t


def main():
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)

    print(path_sum(tree, 22))


if __name__ == '__main__':
    main()
