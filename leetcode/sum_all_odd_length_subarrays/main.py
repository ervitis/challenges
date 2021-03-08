"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
"""
from typing import List


def sum_odd_length_subarrays(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0

    s = 0
    if len(arr) % 2 != 0:
        s += sum(arr)

    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if i + j > len(arr):
                continue
            d = arr[j:i + j]
            if len(d) % 2 != 0:
                s += sum(d)
    return s


if __name__ == '__main__':
    print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))
    print(sum_odd_length_subarrays([1, 2]))
    print(sum_odd_length_subarrays([10, 11, 12]))
