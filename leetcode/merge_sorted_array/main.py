"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal
 to m + n such that it has enough space to hold additional elements from nums2.
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if len(nums2) < 1:
        return

    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1

    if n > 0:
        nums1[:n] = nums2[:n]


if __name__ == '__main__':
    nums = [1, 2, 3, 0, 0, 0]
    merge(nums, 3, [2, 5, 6], 3)
    print(nums)

    nums = [1]
    merge(nums, 1, [], 0)
    print(nums)

    nums = [3, 4, 0, 0]
    merge(nums, 2, [1, 5], 2)
    print(nums)

    nums = [0]
    merge(nums, 0, [1], 1)
    print(nums)
