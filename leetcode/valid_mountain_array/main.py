"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
"""
from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    if len(arr) < 3:
        return False

    max_value_index = arr.index(max(arr))
    if 0 == max_value_index or len(arr) - 1 == max_value_index:
        return False

    for i in range(max_value_index):
        if arr[i] >= arr[i+1]:
            return False

    for i in range(max_value_index+1, len(arr)):
        if arr[i] >= arr[i-1]:
            return False
    return True


if __name__ == '__main__':
    print(valid_mountain_array([2, 1]))
    print(valid_mountain_array([3, 5, 5]))
    print(valid_mountain_array([0, 2, 3, 4, 5, 2, 1, 0]))
