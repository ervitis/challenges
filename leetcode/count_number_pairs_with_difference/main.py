"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

    x if x >= 0.
    -x if x < 0.

"""
from collections import defaultdict
from typing import List


def count_k_difference(nums: List[int], k: int) -> int:
    c = 0
    s = defaultdict(int)
    for num in nums:
        c += s[num - k] + s[num + k]
        s[num] += 1
    return c


def main():
    print(count_k_difference([1, 2, 2, 1], 1))


if __name__ == '__main__':
    main()
