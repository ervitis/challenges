"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    n = len(nums)
    c = n
    i = 0
    while i < len(nums):
        if c <= 0:
            break
        if nums[i] == val:
            n -= 1
            nums.remove(val)
            nums.append(val)
            i -= 1
        c -= 1
        i += 1
    return n


if __name__ == '__main__':
    print(remove_element([3, 2, 2, 3], 3))
    print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(remove_element([1], 1))
