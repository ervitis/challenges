"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
"""

from typing import List
from sys import maxsize


def max_sub_array(nums: List[int]) -> int:
    end = 0
    largest = -maxsize - 1
    for i in range(0, len(nums)):
        end += nums[i]
        if largest < end:
            largest = end
        if end < 0:
            end = 0
    return largest


if __name__ == '__main__':
    print(max_sub_array([1, 2]))
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sub_array([1]))
    print(max_sub_array([0]))
    print(max_sub_array([-1]))
    print(max_sub_array([-10000]))
