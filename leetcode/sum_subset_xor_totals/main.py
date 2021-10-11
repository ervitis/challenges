# -*- coding: utf-8 -*-
from typing import List

"""
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

    For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
"""


def subset_xor_sum(nums: List[int]) -> int:
    bits = 0

    for n in nums:
        bits |= n
    return bits * int(pow(2, len(nums) - 1))


def main():
    print(subset_xor_sum([1, 3]))
    print(subset_xor_sum([5, 1, 6]))


if __name__ == '__main__':
    main()
