"""
https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    f = nums[0]

    for i in range(1, len(nums)):
        if f == 0:
            return False
        f -= 1
        f = max(f, nums[i])

    return True


def main():
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))


if __name__ == '__main__':
    main()
