"""
https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    s = len(nums)
    m_len = s + 1
    i = j = curr = 0

    while j < s:
        while curr < target and j < s:
            curr += nums[j]
            j += 1
        while curr >= target and i < s:
            if m_len > j - i:
                m_len = j - i
            curr -= nums[i]
            i += 1
    if m_len <= s:
        return m_len
    return 0


def main():
    print(min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))
    print(min_sub_array_len(4, [0, 1, 1]))
    print(min_sub_array_len(11, [1, 1, 1, 1, 1, 1, 1]))


if __name__ == '__main__':
    main()
