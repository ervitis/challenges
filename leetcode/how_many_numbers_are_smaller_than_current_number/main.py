"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
"""
from typing import List


def smaller_number_than_current(nums: List[int]) -> List[int]:
    res = {}
    for k, v in enumerate(sorted(nums)):
        if v not in res:
            res[v] = k

    return [res[v] for v in nums]


if __name__ == '__main__':
    print(smaller_number_than_current([8, 1, 2, 2, 3]))
    print(smaller_number_than_current([6, 5, 4, 8]))
