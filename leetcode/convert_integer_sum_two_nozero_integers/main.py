"""
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

    A and B are No-Zero integers.
    A + B = n

It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.
"""
from typing import List


def get_no_zero_integers(n: int) -> List[int]:
    e = 1
    while (n - e) % 10 == 0 or '0' in str(n-e) or '0' in str(e):
        e += 1
    return [e, n - e]


if __name__ == '__main__':
    print(get_no_zero_integers(2))
    print(get_no_zero_integers(11))
    print(get_no_zero_integers(10000))
    print(get_no_zero_integers(1010))
    print(get_no_zero_integers(4102))
