"""
Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
"""
from typing import List


def contains_pattern(arr: List[int], m: int, k: int) -> bool:
    i = 0
    while i < len(arr):
        p = arr[i:i + m]
        if p * k == arr[i:i + m * k]:
            return True
        i += 1
    return False


if __name__ == '__main__':
    print(contains_pattern([1, 2, 4, 4, 4, 4], 1, 3))
    print(contains_pattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2))
