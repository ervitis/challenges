"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.
"""
from typing import List


def find_special_integer(arr: List[int]) -> int:
    d = {}
    for e in arr:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    n = len(arr) * 0.25
    for k, v in d.items():
        if v > n:
            return k
    return -1


if __name__ == '__main__':
    print(find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]))
    print(find_special_integer([1, 2, 2, 7, 10]))
    print(find_special_integer([1, 2, 7, 10]))
