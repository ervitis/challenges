"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] >= target:
            return i
        i += 1
    return i


if __name__ == '__main__':
    print(search_insert([1, 3, 5, 6], 5))
    print(search_insert([1, 3, 5, 6], 2))
    print(search_insert([1, 3, 5, 6], 7))
    print(search_insert([1, 3, 5, 6], 0))
    print(search_insert([1], 0))
    print(search_insert([], 3))
