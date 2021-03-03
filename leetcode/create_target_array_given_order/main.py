"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

    Initially target array is empty.
    From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
    Repeat the previous step until there are no elements to read in nums and index.

Return the target array.

It is guaranteed that the insertion operations will be valid.
"""
from typing import List


def create_target_array(nums: List[int], index: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums

    ta = [-1] * len(nums)
    n = 0

    while n < len(nums):
        ta = ta[:index[n]] + [nums[n]] + ta[index[n]:]
        n += 1
    for i in range(len(ta)-1, 0, -1):
        if ta[i] == -1:
            ta.pop(i)
    return ta


if __name__ == '__main__':
    print(create_target_array([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
    print(create_target_array([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
    print(create_target_array([1], [0]))
