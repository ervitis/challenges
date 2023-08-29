"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)
    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    return k


def main():
    print(remove_duplicates([1, 1, 1, 2, 2, 3]))
    print(remove_duplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(remove_duplicates([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 3, 3]))


if __name__ == '__main__':
    main()
