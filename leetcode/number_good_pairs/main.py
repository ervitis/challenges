"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""
from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    d = {}
    n = 0
    for num in nums:
        if num not in d:
            d[num] = 0
        d[num] += 1

    for _, v in d.items():
        n += (v * (v - 1)) // 2
    return n


if __name__ == '__main__':
    print(num_identical_pairs([1, 2, 3, 1, 1, 3]))
    print(num_identical_pairs([1, 1, 1, 1]))
    print(num_identical_pairs([1, 2, 3]))
