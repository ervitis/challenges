"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

from dataclasses import dataclass
from typing import Type, List


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root


if __name__ == '__main__':
    print(sorted_array_to_bst([-10, -3, 0, 5, 9]))
