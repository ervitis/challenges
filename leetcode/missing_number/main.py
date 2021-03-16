"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
from typing import List


def missing_number(nums: List[int]) -> int:
    d = dict.fromkeys(nums)
    i = 0
    while i < len(nums):
        if i not in d:
            break
        i += 1
    return i


if __name__ == '__main__':
    print(missing_number([3, 0, 1]))
    print(missing_number([0, 1]))
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(missing_number([0]))
