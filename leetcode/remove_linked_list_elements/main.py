"""
Remove all elements from a linked list of integers that have value val.
"""

from dataclasses import dataclass
from typing import Type


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


def remove_elements(head: ListNode, val: int) -> ListNode:
    n = ListNode(-1)
    n.next = head

    pre_node, curr = n, n.next

    while curr:
        if curr.val == val:
            pre_node.next = curr.next
        else:
            pre_node = curr
        curr = curr.next
    return n.next


if __name__ == '__main__':
    print(remove_elements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6))
