"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
"""
from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [f'{nums[0]}']

    ls = []
    for k, v in enumerate(nums):
        if k == 0:
            ls.append(f'{v}')
        elif v == nums[k - 1]:
            continue
        elif v - 1 == nums[k - 1]:
            n = ls[-1].find('->')
            ls[-1] = ls[-1].replace(ls[-1][n + 2:], f'{v}') if n >= 0 else f'{ls[-1]}->{v}'
        else:
            ls.append(f'{v}')
    return ls


if __name__ == '__main__':
    print(summary_ranges([0, 1, 2, 4, 5, 7]))
    print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))
    print(summary_ranges([]))
    print(summary_ranges([-1]))
    print(summary_ranges([0]))
    print(summary_ranges([0, 1, 2, 4, 5, 7, 9, 10, 12, 14, 15, 16, 27, 28]))
