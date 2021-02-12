"""
Reverse a singly linked list
"""

from dataclasses import dataclass
from typing import Type


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


def reverse_list(head: ListNode) -> ListNode:
    rev = None

    while head:
        cur = head
        head = cur.next
        cur.next = rev
        rev = cur
    return rev


if __name__ == '__main__':
    print(reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
