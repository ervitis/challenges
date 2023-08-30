"""
https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
    # nums[:] = list(nums[k:] + nums[:k])

    # another solution
    # while k > 0:
    #     nums[:] = [nums[len(nums) - 1]] + nums[:len(nums) - 1]
    #     k -= 1
    print(nums)


def main():
    rotate([1, 2, 3, 4, 5, 6, 7], 3)
    rotate([-1, -100, 3, 99], 2)


if __name__ == '__main__':
    main()
