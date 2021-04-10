"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    r = set()
    nums1 = set(nums1)
    for num in nums2:
        if num in nums1 and num not in r:
            r.add(num)
    return list(r)


if __name__ == '__main__':
    print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
