"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""
from typing import List


def maximum_product(nums: List[int]) -> int:
    nums = sorted(nums)
    ln = len(nums)
    return max(nums[0] * nums[1] * nums[ln - 1], nums[ln - 1] * nums[ln - 2] * nums[ln - 3])


if __name__ == '__main__':
    print(maximum_product([1, 2, 3]))
    print(maximum_product([1, 2, 3, 4]))
    print(maximum_product([-1, -2, -3]))
    print(maximum_product([-100, -98, -1, 2, 3, 4]))
