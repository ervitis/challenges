"""

"""

from dataclasses import dataclass
from typing import Type


@dataclass
class TreeNode(object):
    val: int
    left: Type['TreeNode'] = None
    right: Type['TreeNode'] = None


def tree_2_str(t: TreeNode) -> str:
    if not t:
        return ''

    root = str(t.val)
    left = tree_2_str(t.left)
    right = tree_2_str(t.right)

    if right:
        return root + '(' + left + ')(' + right + ')'
    else:
        if left:
            return root + '(' + left + ')'
        else:
            return root


if __name__ == '__main__':
    print(tree_2_str(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))))
