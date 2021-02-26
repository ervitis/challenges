"""
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.
"""
from typing import List


def sort_by_bits(arr: List[int]) -> List[int]:
    return sorted(arr, key=lambda x: (bin(x).count('1') << 16) + x)


if __name__ == '__main__':
    print(sort_by_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
