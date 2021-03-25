"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
"""
from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    i = 0
    av = sum(nums[i:i+k])
    t = av
    while i + k < len(nums):
        t = t - nums[i] + nums[i+k]
        if t > av:
            av = t
        i += 1
    return av/k


if __name__ == '__main__':
    print(find_max_average([1, 12, -5, -6, 50, 3], 4))
