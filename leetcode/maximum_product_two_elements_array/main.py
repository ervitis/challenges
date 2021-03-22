"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""
from typing import List


def max_product(nums: List[int]) -> int:
    mx = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            n = (nums[i] - 1) * (nums[j] - 1)
            if n > mx:
                mx = n
    return mx


def max_product_2(nums: List[int]) -> int:
    nums = sorted(nums, reverse=True)
    return (nums[0] - 1) * (nums[1] - 1)


if __name__ == '__main__':
    print(max_product([3, 4, 5, 2]))
    print(max_product([1, 5, 4, 5]))
    print(max_product([3, 7]))
    print(max_product_2([3, 4, 5, 2]))
    print(max_product_2([1, 5, 4, 5]))
    print(max_product_2([3, 7]))
