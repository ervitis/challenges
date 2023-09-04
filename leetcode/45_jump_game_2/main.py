"""
https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


def jump(nums: List[int]) -> int:
    l, jumps, curr, far = len(nums), 0, 0, 0

    for i in range(len(nums)-1):
        far = max(far, nums[i] + i)
        if i == curr:
            jumps += 1
            curr = far
            if curr >= l - 1:
                break
    return jumps


def main():
    print(jump([2, 3, 1, 1, 4]))
    print(jump([3, 2, 1, 0, 4]))


if __name__ == '__main__':
    main()
