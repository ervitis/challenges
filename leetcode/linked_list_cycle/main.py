"""

"""

from dataclasses import dataclass
from typing import Type, List


@dataclass
class ListNode(object):
    val: int
    next: Type['ListNode'] = None


def has_cycle(head: ListNode) -> bool:
    if head is None:
        return False

    cur, n = head, head
    while cur and cur.next:
        cur, n = cur.next.next, n.next
        if cur == n:
            return True
    return False


if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n4.next = n2
    n3.next = n4
    n2.next = n3
    n1.next = n2

    h = n1

    print(has_cycle(h))
