"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
from typing import List


def majority_element(nums: List[int]) -> int:
    nums.sort()
    c, max_ele, temp, found = 1, -1, nums[0], False
    e = 0

    for i in range(1, len(nums)):
        if temp == nums[i]:
            c += 1
        else:
            c = 1
            temp = nums[i]

        if max_ele < c:
            max_ele = c
            e = nums[i]

            if max_ele > len(nums) // 2:
                found = True
                break
    return e if found else nums[0]


if __name__ == '__main__':
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([2147483647]))
    print(majority_element([1]))
