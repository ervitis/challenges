"""
The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].

Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
"""
from typing import List


def add_to_array_form(num: List[int], k: int) -> List[int]:
    r = []
    n = ''
    for nu in num:
        n += str(nu)
    n = int(n) + k
    for e in str(n):
        r.append(int(e))
    return r


if __name__ == '__main__':
    print(add_to_array_form([1, 2, 0, 0], 34))
    print(add_to_array_form([2, 7, 4], 181))
    print(add_to_array_form([2, 1, 5], 806))
    print(add_to_array_form([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))
    print(add_to_array_form([9, 9, 9], 1000))
