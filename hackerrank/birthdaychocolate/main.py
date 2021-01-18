# -*- coding: utf-8 -*-


def has_cycle(head):
    if head.next is None:
        return True

    v = [{"isVisited": True, "node": head}]
    nxt = head.next

    while nxt is not None:
        for n in v:
            if n["isVisited"] is True and n["node"] == nxt:
                return True
        v.append({"node": nxt, "isVisited": True})
        nxt = nxt.next
    return False


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


def main():
    list1 = Node(1)
    list1.next = Node(-1)
    list1.next.next = Node(1)
    list1.next.next.next = Node(1)
    
    print(has_cycle(list1))

    list2 = Node(1)
    list2.next = Node(-1)
    list2.next.next = list2
    list2.next.next.next = Node(1)

    print(has_cycle(list2))


if __name__ == '__main__':
    main()
