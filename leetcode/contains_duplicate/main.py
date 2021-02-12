"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    if len(nums) < 2:
        return False

    hm = set()

    for i in nums:
        if i in hm:
            return True
        hm.add(i)
    return False


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
