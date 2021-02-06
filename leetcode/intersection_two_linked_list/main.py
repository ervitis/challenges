"""
Write a program to find the node at which the intersection of two singly linked lists begins
"""

from dataclasses import dataclass
from typing import Type, List


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    curA, curB = headA, headB

    while curA != curB:
        if curA is None:
            curA = headB
        else:
            curA = curA.next
        if curB is None:
            curB = headA
        else:
            curB = curB.next
    return curA


if __name__ == '__main__':
    li = ListNode(8, ListNode(4, ListNode(5)))
    print(get_intersection_node(
        ListNode(4, ListNode(1, li)),
        ListNode(5, ListNode(6, ListNode(1, li)))
    ))
