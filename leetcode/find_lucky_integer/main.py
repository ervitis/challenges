"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""
import collections
from typing import List


def find_lucky(arr: List[int]) -> int:
    s = collections.Counter(arr)
    m = -1
    for k, v in s.items():
        if k == v and m < v:
            m = v
    return m


if __name__ == '__main__':
    print(find_lucky([2, 2, 3, 4]))
    print(find_lucky([1, 2, 2, 3, 3, 3]))
    print(find_lucky([2, 2, 2, 3, 3]))
    print(find_lucky([7, 7, 7, 7, 7, 7, 7]))
