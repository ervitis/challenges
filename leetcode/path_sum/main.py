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


def path_sum(root: TreeNode, sum: int) -> bool:
    if root is None:
        return False
    else:
        if sum == root.val and root.left is None and root.right is None:
            return True
        else:
            return path_sum(root.left, sum - root.val) or path_sum(root.right, sum - root.val)


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
