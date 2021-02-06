"""
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.
"""
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    right = len(numbers) - 1
    left = 0

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
    return [-1, -1]


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 3, 4], 6))
