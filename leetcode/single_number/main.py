"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one
"""
from typing import List


def single_number(nums: List[int]) -> int:
    d = {}
    for e in nums:
        if e in d:
            d.pop(e)
        else:
            d.update({e: 0})
    for k, v in d.items():
        if v == 0:
            return k


if __name__ == '__main__':
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number([1]))
