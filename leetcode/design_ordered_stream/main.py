"""
There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:

    OrderedStream(int n) Constructs the stream to take n values.
    String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.
"""
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.queue = [None] * n
        self.ptr = 0

    def insert(self, id_key: int, value: str) -> List[str]:
        id_key -= 1
        self.queue[id_key] = value
        if id_key == self.ptr:
            while self.ptr < len(self.queue) and self.queue[self.ptr]:
                self.ptr += 1
            return self.queue[id_key:self.ptr]
        return []


if __name__ == '__main__':
    os = OrderedStream(3)
    print(os.insert(3, 'cccc'))
    print(os.insert(1, 'aaaa'))
    print(os.insert(2, 'bbbb'))
