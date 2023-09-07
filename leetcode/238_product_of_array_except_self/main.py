"""
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    c = [0] * n
    c[0] = 1
    # multiply each element of array
    # for example, we will have [1, 1, 2, 6] and [1, -2, -1, 0, 0] in each case of the example
    for i in range(1, n):
        c[i] = nums[i-1] * c[i-1]

    # using a counter we multiply it with each element of the array so we have
    j = 1
    for i in range(n-1, -1, -1):
        c[i] = c[i] * j
        j *= nums[i]

    return c


def main():
    print(product_except_self([1, 2, 3, 4]))
    print(product_except_self([-1, 1, 0, -3, 3]))


if __name__ == '__main__':
    main()
