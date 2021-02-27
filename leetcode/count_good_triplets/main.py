"""
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.

Return the number of good triplets.
"""
from typing import List


def count_good_triplets(arr: List[int], a: int, b: int, c: int) -> int:
    r = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    r += 1
    return r


if __name__ == '__main__':
    print([3, 0, 1, 1, 9, 7], 7, 2, 3)
    print([1, 1, 2, 2, 3], 0, 0, 1)
