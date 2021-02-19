"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""
from dataclasses import dataclass
from typing import Type


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


def middle_node(head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    print(middle_node(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
