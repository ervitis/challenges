"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
"""
from typing import List


def contains_near_by_duplicate(nums: List[int], k: int) -> bool:
    if len(nums) < 2:
        return False

    hm = {}

    for i, n in enumerate(nums):
        if n in hm and i - hm[n] <= k:
            return True
        hm[n] = i

    return False


if __name__ == '__main__':
    print(contains_near_by_duplicate([1, 2, 3, 1], 3))
    print(contains_near_by_duplicate([1, 2, 3, 1, 2, 3], 2))
