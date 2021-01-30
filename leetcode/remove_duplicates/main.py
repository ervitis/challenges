"""
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.
"""
from dataclasses import dataclass
from typing import Type


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


@dataclass
class LinkedList(object):
    node: ListNode = None

    def print(self):
        curr = self.node
        while curr is not None:
            print(curr.val, end='->')
            curr = curr.next

    def add(self, v: int):
        n = ListNode(v)
        n.next = self.node
        self.node = n

    @property
    def get_node(self):
        return self.node


def delete_duplicates(head: ListNode) -> ListNode:
    if head is None:
        return

    curr = head

    while curr.next is not None:
        if curr.val == curr.next.val:
            n = curr.next.next
            curr.next = n
        else:
            curr = curr.next
    return head


if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(3)
    l.print()
    nl = delete_duplicates(l.get_node)

