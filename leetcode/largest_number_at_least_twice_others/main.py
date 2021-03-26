"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
"""
from typing import List


def dominant_index(nums: List[int]) -> int:
    pair = (0, -1)
    idx = -1
    for k, v in enumerate(nums):
        if v > pair[0]:
            if v >= 2 * pair[0]:
                idx = k
            pair = (v, k)
        elif 2 * v > pair[0]:
            idx = -1
    if idx == pair[1]:
        return idx
    return -1


if __name__ == '__main__':
    print(dominant_index([3, 6, 1, 0]))
    print(dominant_index([1, 2, 3, 4]))
    print(dominant_index([0, 0, 3, 2]))
