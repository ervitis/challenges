"""
Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.

It is guaranteed that the node to be deleted is not a tail node in the list.
"""
from dataclasses import dataclass
from typing import Type


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))


def delete_node(node: ListNode):
    global head
    cur = head
    prev = None

    if cur.val == node.val:
        head = cur.next
        cur = None
        return

    while cur:
        if cur.val == node.val:
            break
        prev = cur
        cur = cur.next

    prev.next = cur.next
    cur = None


if __name__ == '__main__':
    delete_node(ListNode(4))
    print(head)
