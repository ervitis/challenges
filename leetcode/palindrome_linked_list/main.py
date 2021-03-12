"""
Given the head of a singly linked list, return true if it is a palindrome.
"""
from dataclasses import dataclass
from typing import Type


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


def is_palindrome(head: ListNode) -> bool:
    left = head

    ln = 0
    while left:
        ln += 1
        left = left.next

    la = []
    left = head
    for i in range(ln//2):
        la.append(left.val)
        left = left.next

    def reverse_list(h):
        prev = None
        curr = h
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    right = reverse_list(head)
    ra = []
    cur = right
    for i in range(ln//2):
        ra.append(cur.val)
        cur = cur.next

    return la == ra


def is_palindrome_queue(head: ListNode) -> bool:
    import collections
    queue = collections.deque()

    cur = head
    while cur:
        queue.append(cur.val)
        cur = cur.next

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True


if __name__ == '__main__':
    print(is_palindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
    print(is_palindrome_queue(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
