"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
"""
from typing import List


def special_array(nums: List[int]) -> int:
    k = -1
    while k <= len(nums):
        c = 0
        for num in nums:
            if num >= k:
                c += 1
        if k == c:
            return k
        k += 1
    return -1


if __name__ == '__main__':
    print(special_array([3, 5]))
    print(special_array([0, 0]))
    print(special_array([0, 4, 3, 0, 4]))
    print(special_array([3, 6, 7, 7, 0]))
    print(special_array([3, 9, 7, 8, 3, 8, 6, 6]))
